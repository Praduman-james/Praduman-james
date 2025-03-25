<div class="casino-container">
    <h1>🎲 Casino Lottery Game 🎲</h1>
    <p>💰 Balance: <span id="balance">500</span></p>

    <button class="button" onclick="depositMoney()">💳 Deposit</button>
    <button class="button" onclick="withdrawMoney()">🏦 Withdraw</button>

    <br><br>

    <div class="casino-table" id="table">
        <!-- Numbers will be added dynamically -->
    </div>

    <br>

    <label for="number">Choose a number (1-100): </label>
    <input type="number" id="number" min="1" max="100" class="input-box">

    <br><br>

    <label for="bet">Enter your bet amount: </label>
    <input type="number" id="bet" min="1" class="input-box">

    <br><br>

    <button class="button" onclick="playGame()">🎰 Play</button>

    <p id="result"></p>
</div>

<script>
    let balance = 500;
    let wins = 0;
    let roundsPlayed = 0;

    function generateTable() {
        const table = document.getElementById("table");
        for (let i = 1; i <= 100; i++) {
            let div = document.createElement("div");
            div.className = "number";
            div.textContent = i;
            table.appendChild(div);
        }
    }

    function depositMoney() {
        let amount = parseInt(prompt("Enter deposit amount:"));
        if (!isNaN(amount) && amount > 0) {
            balance += amount;
            document.getElementById("balance").textContent = balance;
            alert(`💳 You deposited $${amount}!`);
        } else {
            alert("❌ Invalid deposit amount!");
        }
    }

    function withdrawMoney() {
        let amount = parseInt(prompt("Enter withdrawal amount:"));
        if (!isNaN(amount) && amount > 0 && amount <= balance) {
            balance -= amount;
            document.getElementById("balance").textContent = balance;
            alert(`🏦 You withdrew $${amount}!`);
        } else {
            alert("❌ Invalid withdrawal amount or insufficient balance!");
        }
    }

    function playGame() {
        let userNumber = parseInt(document.getElementById("number").value);
        let bet = parseInt(document.getElementById("bet").value);
        let resultDisplay = document.getElementById("result");

        if (isNaN(userNumber) || userNumber < 1 || userNumber > 100) {
            resultDisplay.textContent = "❌ Please choose a valid number between 1 and 100!";
            return;
        }

        if (isNaN(bet) || bet < 1 || bet > balance) {
            resultDisplay.textContent = "❌ Invalid bet amount!";
            return;
        }

        let winningNumber = Math.floor(Math.random() * 100) + 1;
        resultDisplay.textContent = `🎱 The white ball stopped on number: ${winningNumber}`;

        if (userNumber === winningNumber) {
            let winnings = bet * 10;
            balance += winnings;
            wins++;
            resultDisplay.innerHTML += `<br><span class="win">🎉 JACKPOT! You won $${winnings}!</span>`;
        } else {
            balance -= bet;
            resultDisplay.innerHTML += `<br><span class="lose">😢 You lost your bet!</span>`;
        }

        roundsPlayed++;
        document.getElementById("balance").textContent = balance;

        if (balance <= 0) {
            resultDisplay.innerHTML += "<br>💸 You're out of money! Game Over!";
            document.querySelector(".button").disabled = true;
        }
    }

    generateTable();
</script>
