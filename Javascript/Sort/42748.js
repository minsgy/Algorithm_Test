function solution(array, commands) {
    var answer = [];
    for (const command of commands){ //[0] 번째부터 [1] 까지 자르고, 정렬, 그 중에서 [2]번째 숫자
        let arrays = array.slice(command[0]-1, command[1])
        arrays.sort((a, b) => a - b);
        answer.push(arrays[command[2]-1]);
    }
    return answer;
}