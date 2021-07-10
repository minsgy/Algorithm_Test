function solution(numbers, target) {
    let answer = 0;
    dfs(0, 0);
    function dfs(search, value){
        if (search < numbers.length){
            dfs(search + 1, value + numbers[search]);
            dfs(search + 1, value - numbers[search]);
        }
        else {
            if (value == target) answer += 1
        }
    }
    return answer;
}