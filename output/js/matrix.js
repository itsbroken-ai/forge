/**
 * FORGED Matrix - Interactive filtering, search, and technique export
 */

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search');
    if (!searchInput) return;

    const cells = document.querySelectorAll('.technique-cell');
    const columns = document.querySelectorAll('.tactic-column');

    searchInput.addEventListener('input', function() {
        const query = this.value.toLowerCase().trim();

        if (!query) {
            // Show all
            cells.forEach(cell => {
                cell.classList.remove('hidden', 'highlight');
            });
            columns.forEach(col => col.style.display = '');
            return;
        }

        cells.forEach(cell => {
            const id = cell.querySelector('.technique-id')?.textContent?.toLowerCase() || '';
            const name = cell.querySelector('.technique-name')?.textContent?.toLowerCase() || '';

            if (id.includes(query) || name.includes(query)) {
                cell.classList.remove('hidden');
                cell.classList.add('highlight');
            } else {
                cell.classList.add('hidden');
                cell.classList.remove('highlight');
            }
        });

        // Hide empty columns
        columns.forEach(col => {
            const visibleCells = col.querySelectorAll('.technique-cell:not(.hidden)');
            col.style.display = visibleCells.length === 0 ? 'none' : '';
        });
    });

    // Layout toggle
    const layoutBtns = document.querySelectorAll('.layout-btn[data-layout]');
    const matrix = document.querySelector('.matrix');

    if (layoutBtns.length && matrix) {
        const saved = localStorage.getItem('forged-layout');
        if (saved === 'flat') {
            matrix.classList.add('matrix--flat');
            layoutBtns.forEach(btn => {
                btn.classList.toggle('active', btn.dataset.layout === 'flat');
            });
        }

        layoutBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                const layout = this.dataset.layout;
                layoutBtns.forEach(b => b.classList.remove('active'));
                this.classList.add('active');

                if (layout === 'flat') {
                    matrix.classList.add('matrix--flat');
                } else {
                    matrix.classList.remove('matrix--flat');
                }
                localStorage.setItem('forged-layout', layout);
            });
        });
    }

    // Sub-method expand/collapse
    const subBadges = document.querySelectorAll('.sub-method-badge');
    subBadges.forEach(badge => {
        badge.style.cursor = 'pointer';
        badge.title = 'Show sub-methods';
        badge.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            const wrapper = this.closest('.technique-cell-wrapper');
            if (!wrapper) return;
            const subList = wrapper.querySelector('.sub-method-list');
            if (!subList) return;
            subList.classList.toggle('expanded');
            this.title = subList.classList.contains('expanded') ? 'Hide sub-methods' : 'Show sub-methods';
        });
    });

    // Keyboard shortcut: / to focus search
    document.addEventListener('keydown', function(e) {
        if (e.key === '/' && document.activeElement !== searchInput) {
            e.preventDefault();
            searchInput.focus();
        }
        if (e.key === 'Escape') {
            if (exportModal && !exportModal.classList.contains('hidden')) {
                exportModal.classList.add('hidden');
                return;
            }
            searchInput.value = '';
            searchInput.dispatchEvent(new Event('input'));
            searchInput.blur();
        }
    });

    // ==========================================
    // SELECTION MODE & EXPORT
    // ==========================================

    const selectBtn = document.getElementById('select-mode-btn');
    const exportBar = document.getElementById('export-bar');
    const exportCount = document.getElementById('export-count');
    const exportGenerate = document.getElementById('export-generate');
    const exportModal = document.getElementById('export-modal');
    const exportClose = document.getElementById('export-close');
    const exportOutput = document.getElementById('export-output');
    const exportCopy = document.getElementById('export-copy');
    const exportDownload = document.getElementById('export-download');

    if (!selectBtn) return;

    let selectMode = false;
    const selectedTechniques = new Set();
    const selectedSubMethods = new Set();

    // Toggle selection mode
    selectBtn.addEventListener('click', function() {
        selectMode = !selectMode;
        this.textContent = selectMode ? 'select: on' : 'select: off';
        this.classList.toggle('active', selectMode);
        matrix.classList.toggle('select-mode', selectMode);
        document.body.classList.toggle('select-mode-active', selectMode);

        if (selectMode) {
            injectCheckboxes();
        } else {
            removeCheckboxes();
            selectedTechniques.clear();
            selectedSubMethods.clear();
            updateExportBar();
        }
    });

    function injectCheckboxes() {
        const wrappers = document.querySelectorAll('.technique-cell-wrapper');
        wrappers.forEach(wrapper => {
            const techCell = wrapper.querySelector('.technique-cell');
            if (!techCell) return;
            const techId = techCell.querySelector('.technique-id')?.textContent?.trim();
            if (!techId) return;

            // Technique checkbox
            const cb = document.createElement('input');
            cb.type = 'checkbox';
            cb.className = 'technique-checkbox';
            cb.dataset.techId = techId;
            cb.addEventListener('change', function(e) {
                e.stopPropagation();
                handleTechniqueCheck(techId, this.checked, wrapper);
            });
            cb.addEventListener('click', function(e) {
                e.stopPropagation();
            });
            wrapper.appendChild(cb);

            // Sub-method checkboxes
            const subRows = wrapper.querySelectorAll('.sub-method-row');
            subRows.forEach(row => {
                const subId = row.querySelector('.sub-method-id')?.textContent?.trim();
                if (!subId) return;

                const subCb = document.createElement('input');
                subCb.type = 'checkbox';
                subCb.className = 'sub-method-checkbox';
                subCb.dataset.subId = subId;
                subCb.dataset.parentId = techId;
                subCb.addEventListener('change', function(e) {
                    e.stopPropagation();
                    handleSubMethodCheck(subId, techId, this.checked, wrapper);
                });
                subCb.addEventListener('click', function(e) {
                    e.stopPropagation();
                    e.preventDefault();
                    this.checked = !this.checked;
                    this.dispatchEvent(new Event('change'));
                });
                row.insertBefore(subCb, row.firstChild);
            });
        });
    }

    function removeCheckboxes() {
        document.querySelectorAll('.technique-checkbox, .sub-method-checkbox').forEach(cb => cb.remove());
        document.querySelectorAll('.technique-cell-wrapper.selected').forEach(w => w.classList.remove('selected'));
    }

    function handleTechniqueCheck(techId, checked, wrapper) {
        if (checked) {
            selectedTechniques.add(techId);
            wrapper.classList.add('selected');
            // Auto-select all sub-methods
            const subCbs = wrapper.querySelectorAll('.sub-method-checkbox');
            subCbs.forEach(cb => {
                cb.checked = true;
                selectedSubMethods.add(cb.dataset.subId);
            });
        } else {
            selectedTechniques.delete(techId);
            wrapper.classList.remove('selected');
            // Deselect all sub-methods
            const subCbs = wrapper.querySelectorAll('.sub-method-checkbox');
            subCbs.forEach(cb => {
                cb.checked = false;
                selectedSubMethods.delete(cb.dataset.subId);
            });
        }
        updateExportBar();
    }

    function handleSubMethodCheck(subId, parentId, checked, wrapper) {
        if (checked) {
            selectedSubMethods.add(subId);
            // Auto-select parent technique
            if (!selectedTechniques.has(parentId)) {
                selectedTechniques.add(parentId);
                wrapper.classList.add('selected');
                const parentCb = wrapper.querySelector('.technique-checkbox');
                if (parentCb) parentCb.checked = true;
            }
        } else {
            selectedSubMethods.delete(subId);
            // If no sub-methods remain selected, don't auto-deselect parent
            // (user may want the technique without specific sub-methods)
        }
        updateExportBar();
    }

    function updateExportBar() {
        const count = selectedTechniques.size;
        if (count > 0) {
            exportBar.classList.remove('hidden');
            exportCount.textContent = count === 1 ? '1 method selected' : count + ' methods selected';
        } else {
            exportBar.classList.add('hidden');
        }
    }

    // Generate export
    let lastBlobUrl = null;
    exportGenerate.addEventListener('click', function() {
        const md = generateMarkdown();
        exportOutput.textContent = md;
        exportModal.classList.remove('hidden');

        // Revoke previous Blob URL to prevent memory leak
        if (lastBlobUrl) URL.revokeObjectURL(lastBlobUrl);
        const blob = new Blob([md], { type: 'text/markdown' });
        lastBlobUrl = URL.createObjectURL(blob);
        exportDownload.href = lastBlobUrl;
    });

    // Close modal
    exportClose.addEventListener('click', function() {
        exportModal.classList.add('hidden');
    });

    exportModal.addEventListener('click', function(e) {
        if (e.target === exportModal) {
            exportModal.classList.add('hidden');
        }
    });

    // Copy to clipboard
    exportCopy.addEventListener('click', function() {
        const btn = this;
        const text = exportOutput.textContent;
        navigator.clipboard.writeText(text).then(() => {
            btn.textContent = 'Copied!';
            btn.classList.add('copied');
            setTimeout(() => {
                btn.textContent = 'Copy to Clipboard';
                btn.classList.remove('copied');
            }, 2000);
        }).catch(() => {
            btn.textContent = 'Copy failed';
            setTimeout(() => { btn.textContent = 'Copy to Clipboard'; }, 2000);
        });
    });

    function generateMarkdown() {
        // Load framework data
        const dataEl = document.getElementById('framework-data');
        if (!dataEl) return '# Error: Framework data not found';

        let data;
        try {
            data = JSON.parse(dataEl.textContent);
        } catch (e) {
            return '# Error: Could not parse framework data';
        }

        const tactics = data.tactics;
        const techniques = data.techniques;
        const fw = data.framework;

        // Build lookup maps
        const techMap = {};
        techniques.forEach(t => { techMap[t.id] = t; });

        const tacticMap = {};
        tactics.forEach(t => { tacticMap[t.id] = t; });

        // Group selected techniques by tactic
        const byTactic = {};
        selectedTechniques.forEach(techId => {
            const tech = techMap[techId];
            if (!tech) return;
            if (!byTactic[tech.tactic_id]) {
                byTactic[tech.tactic_id] = [];
            }
            byTactic[tech.tactic_id].push(tech);
        });

        // Build markdown
        let md = '# F.O.R.G.E. — Selected Methods\n\n';
        md += '> ' + fw.full_name + '\n';
        md += '> Source: https://forged.itsbroken.ai | Version ' + fw.version + '\n\n';
        md += '---\n';

        // Iterate tactics in order
        tactics.forEach(tactic => {
            const techs = byTactic[tactic.id];
            if (!techs || techs.length === 0) return;

            md += '\n## ' + tactic.id + ': ' + tactic.name + '\n';

            techs.forEach(tech => {
                md += '\n### ' + tech.id + ': ' + tech.name + '\n';

                if (tech.description) {
                    md += '\n**Description:** ' + tech.description + '\n';
                }

                if (tech.implementation) {
                    md += '\n**Implementation:** ' + tech.implementation + '\n';
                }

                if (tech.success_indicators && tech.success_indicators.length > 0) {
                    md += '\n**Success Indicators:**\n';
                    tech.success_indicators.forEach(ind => {
                        md += '- ' + ind + '\n';
                    });
                }

                if (tech.failure_modes && tech.failure_modes.length > 0) {
                    md += '\n**Failure Modes:**\n';
                    tech.failure_modes.forEach(fm => {
                        md += '- ' + fm + '\n';
                    });
                }

                // Sub-methods: only include selected ones
                const subs = tech.sub_methods || [];
                if (subs.length > 0) {
                    const selectedSubs = subs.filter(s => selectedSubMethods.has(s.id));
                    if (selectedSubs.length > 0) {
                        md += '\n#### Sub-Methods\n';
                        selectedSubs.forEach(sub => {
                            md += '\n**' + sub.id + ': ' + sub.name + '**\n';
                            md += sub.description + '\n';
                        });
                    }
                }

                md += '\n---\n';
            });
        });

        return md;
    }
});
