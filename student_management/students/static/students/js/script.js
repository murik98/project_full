document.addEventListener('DOMContentLoaded', function() {
    // Инициализация компонентов Bootstrap
    initBootstrapComponents();
    
    // Обработчики событий
    setupEventHandlers();
});

function initBootstrapComponents() {
    // Инициализация всплывающих подсказок
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl, {
            trigger: 'hover focus'
        });
    });

    // Инициализация popover
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
}

function setupEventHandlers() {
    // Подтверждение удаления
    document.querySelectorAll('.confirm-delete').forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Вы уверены, что хотите удалить эту запись? Это действие нельзя отменить.')) {
                e.preventDefault();
            }
        });
    });

    // Превью загружаемых изображений
    document.querySelectorAll('.image-upload').forEach(input => {
        input.addEventListener('change', function() {
            const file = this.files[0];
            const previewId = this.dataset.preview;
            const preview = document.getElementById(previewId);
            
            if (file && preview) {
                if (!file.type.match('image.*')) {
                    alert('Пожалуйста, выберите файл изображения');
                    this.value = '';
                    return;
                }

                const reader = new FileReader();
                reader.onload = function(e) {
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                }
                reader.readAsDataURL(file);
            }
        });
    });

    // Динамическое обновление заголовков форм
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Обработка...';
            }
        });
    });
}

// Вспомогательные функции
function showToast(message, type = 'success') {
    // Реализация toast-уведомлений
}