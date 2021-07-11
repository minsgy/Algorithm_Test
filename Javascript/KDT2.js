let isPositive = (num) => {
    return num >= 0;
  };
  
  function solution(deposit) {
      let answer = [];
      
      for (let history of deposit){
          if (isPositive(history)){
              answer.push(history);
          } 
          else {
              let deposit_money = history;
              while(deposit_money < 0){
                  let money = answer.pop();
                  if (money + deposit_money >= 0){
                      let result = money + deposit_money;
                      if (result == 0){ break; }
                      answer.push(result);
                      break;
                  }
                  else {
                      deposit_money += money;
                  }
              }
          }
      }
      
      
      
      return answer;
  }