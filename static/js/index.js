document.addEventListener("DOMContentLoaded", ready);

function ready() {
    const copyBtn = document.querySelector("#copy-ip-btn");

    const ipText = document.querySelector(".ip-address");

    copyBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(ipText.textContent);
    });
}