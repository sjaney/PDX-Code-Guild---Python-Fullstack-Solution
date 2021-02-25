let app = new Vue({
    el: '#app',
    data: {
        computerOptions: ['rock','paper','scissors'],
        userInput: '',
        whoWins: '',
        random: ''
    },
    methods: {
        playGame: function() {
            this.computerPick() 

            if (this.random === 'rock' && this.userInput === 'paper'){
                this.whoWins = "Computer picks rock. You Win!" 
            } else if (this.random === 'rock' && this.userInput === 'scissors'){
                this.whoWins = "Computer picks rock. You lose!"
            }else if (this.random === 'paper' && this.userInput === 'rock'){
                this.whoWins = "Computer picks paper. You lost!"
            } else if (this.random=== 'paper' && this.userInput === 'scissors'){
                this.whoWins = "Computer picks paper. You win!"
            } else if (this.random === 'scissors' && this.userInput === 'rock'){
                this.whoWins = "Computer picks scissors. You win!"
            } else if (this.random === 'scissors' && this.userInput === 'paper'){
                this.whoWins = "Computer picks scissors. You lose!"
            } else {
                this.whoWins = (`Computer picks ${this.random}. You tie!`)
            }
        },
        computerPick: function() {
            this.random = this.computerOptions[Math.floor(Math.random() * this.computerOptions.length)]
        }
    }
    
})  