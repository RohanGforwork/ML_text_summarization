// script.js
let isProcessing = false;

function openPopup() {
    const popup = document.getElementById("popup");
    const content = document.querySelector(".popup-content");
    
    popup.style.display = "flex";
    setTimeout(() => {
        popup.style.opacity = "1";
        content.style.transform = "scale(1)";
        content.classList.add("active");
    }, 10);
}

function closePopup() {
    const popup = document.getElementById("popup");
    const content = document.querySelector(".popup-content");
    
    popup.style.opacity = "0";
    content.style.transform = "scale(0.8)";
    content.classList.remove("active");
    
    setTimeout(() => {
        popup.style.display = "none";
    }, 300);
}

function summarizeText() {
    if (isProcessing) return;
    
    const inputText = document.getElementById("inputText").value;
    const summaryBox = document.getElementById("summaryBox");
    const resultBox = document.getElementById("resultBox");
    
    if (inputText.length > 1000) {
        alert("Text exceeds 1000 character limit!");
        return;
    }
    
    isProcessing = true;
    showLoading(true);
    
    // Simulate API call with better animation
    setTimeout(() => {
        const summarized = inputText.length > 100 ? 
            inputText.substring(0, 100) + "..." : 
            inputText;
        
        animateResult(summaryBox, summarized);
        animateResult(resultBox, `Characters: ${inputText.length} | Words: ${inputText.split(/\s+/).filter(Boolean).length}`);
        isProcessing = false;
        showLoading(false);
    }, 1500);
}

function animateResult(element, text) {
    element.style.opacity = "0";
    element.style.transform = "translateY(10px)";
    setTimeout(() => {
        element.textContent = text;
        element.style.opacity = "1";
        element.style.transform = "translateY(0)";
    }, 200);
}

function showLoading(show) {
    const loader = document.querySelector(".loader") || createLoader();
    loader.style.display = show ? "block" : "none";
}

function createLoader() {
    const loader = document.createElement("div");
    loader.className = "loader";
    loader.innerHTML = `
        <div class="spinner"></div>
    `;
    document.querySelector(".popup-content").appendChild(loader);
    return loader;
}

// Event Listeners
document.getElementById("inputText").addEventListener("input", () => {
    if (!isProcessing) summarizeText();
});

// Close popup when clicking outside
document.getElementById("popup").addEventListener("click", (e) => {
    if (e.target === document.getElementById("popup")) {
        closePopup();
    }
});