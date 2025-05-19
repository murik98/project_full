// static/students/js/search.js
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('input[name="q"]');
    
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const query = e.target.value;
            const url = new URL(window.location.href);
            
            if (query.length > 2 || query.length === 0) {
                url.searchParams.set('q', query);
                window.history.pushState({}, '', url);
                
                // AJAX-запрос (или просто submit формы)
                fetch(url, {
                    headers: { 'X-Requested-With': 'XMLHttpRequest' }
                })
                .then(response => response.text())
                .then(html => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    document.querySelector('tbody').innerHTML = 
                        doc.querySelector('tbody').innerHTML;
                    document.querySelector('.pagination').innerHTML = 
                        doc.querySelector('.pagination')?.innerHTML || '';
                });
            }
        });
    }
});