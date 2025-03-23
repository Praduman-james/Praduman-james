<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Casino Lottery Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #2b2b2b;
            color: white;
        }
        .casino-table {
            display: grid;
            grid-template-columns: repeat(10, 1fr);
            gap: 5px;
            max-width: 500px;
            margin: 20px auto;
        }
        .number {
            padding: 10px;
            background: gold;
            border-radius: 5px;
            font-weight: bold;
        }
        .button {
            padding: 10px 20px;
            background-color: green;
            color: white;
            border: none;
            cursor: pointer;
            margin-top: 10px;
            font-size: 16px;
        }
        .button:disabled {
            background-color: gray;
            cursor: not-allowed;
        }
    </style>
</head>
<body>

    <h1>🎲 Casino Lottery Game 🎲</h1>
    <p>💰 Balance: <span id="balance">500</span></p>

    <div class="casino-table" id="table">
        <!-- Numbers will be added dynamically -->
    </div>

    <label for="number">Choose a number (1-100): </label>
    <input type="number" id="number" min="1" max="100">
    
    <br>

    <label for="bet">Enter your bet amount: </label>
    <input type="number" id="bet" min="1">
    
    <br>
    
    <button class="button" onclick="playGame()">Play</button>

    <p id="result"></p>

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
                resultDisplay.innerHTML += `<br>🎉 JACKPOT! You won $${winnings}!`;
            } else {
                balance -= bet;
                resultDisplay.innerHTML += `<br>😢 You lost your bet!`;
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

</body>
</html>
