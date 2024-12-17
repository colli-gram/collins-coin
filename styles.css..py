body {
    font-family: 'Arial', sans-serif;
    background-color: #1f1f1f;
    color: white;
    margin: 0;
    padding: 0;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.container {
    width: 90%;
    margin: 0 auto;
    text-align: center;
    padding: 20px;
    max-width: 500px;
}

.hidden {
    display: none;
}

h1, h2 {
    color: #ffd700;
}

input, button {
    margin: 10px 0;
    padding: 15px;
    font-size: 18px;
    border: none;
    border-radius: 10px;
}

button {
    background-color: #ff9900;
    color: black;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #cc7a00;
}

/* Mining Circle */
#mining-circle {
    width: 250px;
    height: 250px;
    background-color: #ffd700;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 32px;
    font-weight: bold;
    margin: 20px auto;
    cursor: pointer;
    transition: transform 1s linear;
}

#mining-circle.active {
    animation: rotate 2s infinite linear;
}

#mining-circle:hover {
    background-color: #ffcc00;
}

/* Amount Bar */
.amount-bar {
    background-color: #333;
    padding: 15px;
    margin: 20px;
    font-size: 28px;
    font-weight: bold;
    border-radius: 10px;
}

/* Buttons Styling */
.bottom-btn {
    width: 100%;
    padding: 20px;
    font-size: 20px;
    border-radius: 10px;
    margin-top: 20px;
}

/* Animated Circle */
@keyframes rotate {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}
/* Glowing and Blinking Button */
.glow-blink {
    background-color: #ff9900; /* Button base color */
    color: black;
    padding: 15px 30px;
    font-size: 20px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    text-align: center;
    box-shadow: 0 0 10px rgba(255, 255, 0, 0.7);
    animation: blinkGlow 1.5s infinite; /* Attach the animation */
    transition: all 0.3s ease;
}

/* Button Hover Effect */
.glow-blink:hover {
    background-color: #ffd700; /* Change color on hover */
    box-shadow: 0 0 20px rgba(255, 255, 0, 1);
}

/* Lightning Animation */
@keyframes blinkGlow {
    0%, 100% {
        box-shadow: 0 0 5px rgba(255, 255, 0, 0.4);
    }
    50% {
        box-shadow: 0 0 20px rgba(255, 255, 0, 1);
    }
}
