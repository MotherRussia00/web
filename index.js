// Создать наблюдателя
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        const texts = [entry.target];
        //const texts = entry.target.querySelectorAll(".square");
        if (entry.isIntersecting) {
            texts.forEach(text => { text.classList.add("text-animation"); });
            return;
        }
        // перемещение завершено, теперь надо удалить класс
        texts.forEach(text => { text.classList.remove("text-animation"); });
    });
});

document.addEventListener("DOMContentLoaded", ready);

function ready() {
    const texts = document.querySelectorAll(".animated-text");
    texts.forEach(text => {
        observer.observe(text);
    });
}