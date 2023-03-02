// Создать наблюдателя
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        const texts = entry.target.querySelectorAll(".animation-left");
        //const texts = entry.target.querySelectorAll(".square");
        if (entry.isIntersecting) {
            const time = 200;
            var t = 0;
            texts.forEach(text => {
                setTimeout(() => { text.classList.add("animation-center") }, t);
                t += time;
            });
            return;
        }
        // перемещение завершено, теперь надо удалить класс
        texts.forEach(text => { text.classList.remove("animation-center"); });
    });
});

document.addEventListener("DOMContentLoaded", ready);

function ready() {
    const texts = document.querySelectorAll(".animation-trigger");
    texts.forEach(text => {
        observer.observe(text);
    });
}

const copyBtn = document.querySelector("#copy-ip-btn");

const ipText = document.querySelector(".ip-address");

copyBtn.addEventListener('click', () => {
    navigator.clipboard.writeText(ipText.textContent);
});