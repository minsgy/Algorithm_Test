function solution(answers) {
    let answer = [];
    
    let number_1 = [1,2,3,4,5];
    let number_2 = [2,1,2,3,2,4,2,5];
    let number_3 = [3,3,1,1,2,2,4,4,5,5];
    let count = [0, 0, 0];
    for (let solutions in answers){
        let number_1_len = solutions % 5;
        let number_2_len = solutions % 8;
        let number_3_len = solutions % 10;

        if (number_1[number_1_len] == answers[solutions]){
            count[0] += 1;
        } 
        if (number_2[number_2_len] == answers[solutions]){
            count[1] += 1;
        } 
        if (number_3[number_3_len] == answers[solutions]){
            count[2] += 1;
        } 
    }

    console.log(count)
    
    // 최대값
    const max_number = count.reduce((a, b) => {
            return a > b ? a : b;
    })

    for(let num in count){
        if(count[num] == max_number){
            answer.push(parseInt(num)+1);
        } 
    }
    
    
    return answer;
}