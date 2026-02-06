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
