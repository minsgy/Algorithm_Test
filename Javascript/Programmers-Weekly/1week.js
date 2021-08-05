function solution(price, money, count) {
    let sum = 0;
    let result = 0;
    for(let i=0;i<count;i++){
        sum += price;
        result += sum; 
    }
    return (result-money > 0) ? result-money : 0;
}

solution[3, 20, 4] // 4