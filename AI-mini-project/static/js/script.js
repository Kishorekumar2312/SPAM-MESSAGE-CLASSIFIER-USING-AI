document.getElementById('spamForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const message = document.getElementById('message').value;
    const resultBox = document.getElementById('result-box');
    const resultText = document.getElementById('result');

    const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    });

    const data = await response.json();
    resultBox.style.display = 'block';

    if (data.prediction === 'Spam') {
        resultBox.className = 'spam';
        resultText.textContent = '🚨 This message is SPAM!';
    } else {
        resultBox.className = 'not-spam';
        resultText.textContent = '✅ This message is SAFE.';
    }
});
