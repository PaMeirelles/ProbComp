roll_double_dice <- function(){
    dice <- c(1, 2, 3, 4, 5, 6)
    return(sample(dice, 1) + sample(dice, 1))
}

simulation <- function(n){
    total_tries <- rep(0, n)
    for (i in 0:n){
        tries <- 0
        rolls <- rep(0,11)
        while(TRUE){
            tries = tries + 1
            roll <- roll_double_dice()
            rolls[roll - 1] = 1
            if (rolls == rep(1, 11)){
                break
            } 
        }
        total_tries[i] = tries
    }
    print(sum(total_tries) / n)
}

simulation(10000)