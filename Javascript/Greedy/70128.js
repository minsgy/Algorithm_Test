function solution(a, b) {
    let answer = [];
    for (let i in a){
        answer.push(a[i]*b[i]);
    }
    return answer.reduce(function add(sum, cur){
        return sum + cur;
    })
}