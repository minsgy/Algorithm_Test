function solution(numbers) {
    let answer = [];
    let result = []; 
    let temp = [];
    for(let number of numbers){
        for(let i=0;i<3;i++){
            temp.push(number);
        }
        result.push({'sort_num':temp.join(''), 'real': number});
                    
        temp = [];
    }
    
    // 정렬 할 변수 기준 정렬
    result.sort((a, b) => {
        return b.sort_num < a.sort_num ? -1 : a.sort_num < b.sort_num ? 1 : 0;
    });
    
    for ( let j of result){
        answer.push(String(j.real));
    }  

    // Every 함수를 통해 number 값이 전부 '0' 이라면 0이 반환 되게함.
    return answer = answer.every(v => v == '0') ? '0' : answer.join('');
}