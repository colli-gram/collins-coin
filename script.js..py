let userData = {};
let currentUser = null;
let miningActive = false;
let miningAmount = 0;
let interval;

function startApp() {
    document.getElementById('start-page').classList.add('hidden');
    document.getElementById('registration-page').classList.remove('hidden');
}

function continueRegistration() {
    let name = document.getElementById('user-name').value.trim();
    let phone = document.getElementById('user-phone').value.trim();
    let password = document.getElementById('user-password').value.trim();
    if (name && phone && password) {
        currentUser = name;
        userData[currentUser] = { phone, password, coins: 0, history: [] };
        saveData();
        document.getElementById('registration-page').classList.add('hidden');
        document.getElementById('loading-page').classList.remove('hidden');
        startLoading();
    } else {
        alert("Please fill all the fields.");
    }
}

function startLoading() {
    let countdown = 5;
    const countdownElement = document.getElementById('countdown');
    const countdownInterval = setInterval(() => {
        countdownElement.innerText = countdown;
        countdown--;
        if (countdown < 0) {
            clearInterval(countdownInterval);
            document.getElementById('loading-page').classList.add('hidden');
            document.getElementById('mining-page').classList.remove('hidden');
            document.getElementById('username-display').innerText = currentUser;
        }
    }, 1000);
}

function toggleMining() {
    if (!miningActive) {
        startMining();
    } else {
        stopMining();
    }
}

function startMining() {
    miningActive = true;
    document.getElementById('mining-circle').classList.add('active');
    interval = setInterval(() => {
        miningAmount++;
        document.getElementById('mining-count').innerText = miningAmount;
        if (miningAmount >= 1000) {
            stopMining();
        }
    }, 1000);
}

function stopMining() {
    clearInterval(interval);
    miningActive = false;
    userData[currentUser].coins += miningAmount;
    saveData();
    updateCoinAmount();
    document.getElementById('mining-circle').classList.remove('active');
    document.getElementById('mining-count').innerText = 'Start Mining';
    miningAmount = 0;
}

function updateCoinAmount() {
    document.getElementById('amount-bar').innerText = `${userData[currentUser].coins} CM`;
}

function goToWallet() {
    document.getElementById('mining-page').classList.add('hidden');
    document.getElementById('wallet-page').classList.remove('hidden');
    document.getElementById('amount-bar').innerText = `${userData[currentUser].coins} CM`;
}

function comingSoon() {
    alert("Withdraw feature coming soon!");
}

function sendCoin() {
    document.getElementById('wallet-page').classList.add('hidden');
    document.getElementById('send-page').classList.remove('hidden');
}

function confirmSend() {
    const amount = parseInt(document.getElementById('send-amount').value);
    const recipient = document.getElementById('send-recipient').value;

    if (isNaN(amount) || amount <= 0) {
        alert("Invalid amount.");
        return;
    }

    if (!userData[recipient]) {
        alert("Recipient does not exist.");
        return;
    }

    if (userData[currentUser].coins < amount) {
        alert("Insufficient coins.");
        return;
    }

    userData[currentUser].coins -= amount;
    userData[recipient].coins += amount;
    userData[currentUser].history.push(`Sent ${amount} CM to ${recipient}`);
    saveData();
    document.getElementById('send-page').classList.add('hidden');
    document.getElementById('wallet-page').classList.remove('hidden');
    alert(`Sent ${amount} CM to ${recipient}`);
}

function backToMining() {
    document.getElementById('wallet-page').classList.add('hidden');
    document.getElementById('mining-page').classList.remove('hidden');
}

function saveData() {
    localStorage.setItem('userData', JSON.stringify(userData));
}
// Function to navigate back to the Mining Page from the Wallet Page
function backToMining() {
    // Hide the wallet page
    document.getElementById("wallet-page").classList.add("hidden");
    // Show the mining page
    document.getElementById("mining-page").classList.remove("hidden");
}

// Function to navigate back to the Wallet Page from the Send Page
function backToWallet() {
    // Hide the send page
    document.getElementById("send-page").classList.add("hidden");
    // Show the wallet page
    document.getElementById("wallet-page").classList.remove("hidden");
}
