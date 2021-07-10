// 순열
function permutation(arr, selectNum) {
    let result = [];
    if (selectNum === 1) return arr.map((v) => [v]);
  
    arr.forEach((v, idx, arr) => {
      const fixer = v;
      const restArr = arr.filter((_, index) => index !== idx);
      const permuationArr = permutation(restArr, selectNum - 1);
      const combineFixer = permuationArr.map((v) => [fixer, ...v]);
      result.push(...combineFixer);
    });
    return result;
  }
  
  // N의 제곱근 까지 나눠준다 2부터 n의 제곱근까지 
  function is_prime_number(n) {
      let none_number = [0, 1];
      let number = parseInt(n)
      if(none_number.includes(number)){
          return false;
      }
      else{
          let sqrt_number = parseInt(number**(1/2));
          for(let i=2;i<=sqrt_number;i++){
              if (number % i == 0) return false;
          }
          return true;
      }
  }
  
  function solution(numbers) {
      let result = [];
      let num = [...numbers];
      
      for (let i=1; i<=num.length;i++) {
          let temp = permutation(num, i);
          temp.forEach(v => 
              is_prime_number(parseInt(v.join(''))) ? result.push(parseInt(v.join(''))) :
              result);
      }
      console.log([...new Set(result)])
      return [...new Set(result)].length;
  }
  
