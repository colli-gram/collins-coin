<html><head> 
  <meta charset="UTF-8"> 
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
  <title>Collins Miner</title> 
  <link rel="stylesheet" href="styles.css"> 
 </head> 
 <body> <!-- Start Page --> 
  <div class="container" id="start-page"> 
   <h1>Welcome to Collins Miner</h1> <!-- Start Button with Glow --> <button class="btn glow-blink" onclick="startApp()">Start</button> 
  </div> <!-- Registration Page --> 
  <div class="container hidden" id="registration-page"> 
   <h2>Register</h2> 
   <input type="text" id="user-name" placeholder="Name"> 
   <input type="text" id="user-phone" placeholder="Phone Number"> 
   <input type="password" id="user-password" placeholder="Password"> <!-- Continue Button with Glow --> <button class="btn glow-blink" onclick="continueRegistration()">Continue</button> 
  </div> <!-- Loading Page --> 
  <div class="container hidden" id="loading-page"> 
   <h2>Loading Collins Miner...</h2> 
   <p id="countdown">5</p> 
  </div> <!-- Mining Page --> 
  <div class="container hidden" id="mining-page"> 
   <h2>Hello, <span id="username-display"></span></h2> <!-- Mining Circle --> 
   <div id="mining-circle" class="mining-circle" onclick="toggleMining()"> <span id="mining-count">0</span> CM 
   </div> <!-- Wallet Button with Glow --> <button class="btn glow-blink bottom-btn" id="wallet-btn" onclick="goToWallet()">Wallet</button> 
  </div> <!-- Wallet Page --> 
  <div class="container hidden" id="wallet-page"> 
   <h2>Wallet</h2> 
   <div id="amount-bar" class="amount-bar">
     0 CM 
   </div> <!-- Withdraw and Send Buttons with Glow --> <button class="btn glow-blink bottom-btn" id="withdraw-btn" onclick="comingSoon()">Withdraw</button> <button class="btn glow-blink bottom-btn" id="send-btn" onclick="sendCoin()">Send</button> <!-- Back to Mining Button with Glow --> <button class="btn glow-blink bottom-btn" onclick="backToMining()">Back to Mining</button> 
  </div> <!-- Send Coin Page --> 
  <div class="container hidden" id="send-page"> 
   <h2>Send Collins Coin</h2> 
   <input type="number" id="send-amount" placeholder="Amount to Send"> 
   <input type="text" id="send-recipient" placeholder="Recipient User ID"> <!-- Send Button with Glow --> <button class="btn glow-blink" onclick="confirmSend()">Send</button> <!-- Back to Wallet Button with Glow --> <button class="btn glow-blink" onclick="backToWallet()">Back</button> 
  </div> <!-- Script --> 
  <script src="script.js"></script> 
 

</body></html>
