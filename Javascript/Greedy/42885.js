function solution(people, limit) {
    var answer = 0;
    
    // 오름차순 정렬
    people.sort((a, b) => a - b);
    
    // 시작 Flag
    let left = 0;
    let right = people.length - 1;
    
    while(left < right){
        if (limit >= people[left] + people[right]){
            left += 1;
            right -= 1;
            answer += 1;
        }
        else{
            right -= 1;
            answer += 1;
        }
    }
    if (left == right){
        answer += 1;
    }
    
    
    return answer;
}