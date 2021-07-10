function solution(progresses, speeds) {
    let answer = [];
    let count = 0;
    
    while(progresses.length > 0){
        if (progresses[0] >= 100){ 
            progresses.shift();
            speeds.shift();
            count += 1; 
        } else if (count > 0) {
            answer.push(count);
            count = 0;
        } else {
            for (let i in progresses) progresses[i] += speeds[i];
        }
    }
    answer.push(count);
    return answer;
}