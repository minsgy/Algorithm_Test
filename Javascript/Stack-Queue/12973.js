function solution(s)
{
    let answer = 0;
    let stack = [];
    
    let s_stack = s.split('');
    
    for (let i of s_stack){
        if (stack.length == 0) stack.push(i);
        else if (stack[stack.length - 1] == i) stack.pop();
        else { stack.push(i); }
    }
    return stack.length == 0 ? 1 : 0;
}

console.log(solution('baabaa'));