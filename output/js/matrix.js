/**
 * FORGED Matrix - Interactive filtering and search
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
    const layoutBtns = document.querySelectorAll('.layout-btn');
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
            searchInput.value = '';
            searchInput.dispatchEvent(new Event('input'));
            searchInput.blur();
        }
    });
});
