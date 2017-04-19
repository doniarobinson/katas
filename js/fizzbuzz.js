/**
 *
 * Prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
 *
 */


function fizzbuzz() {
  var output;
  
  for(var i=1;i<=100;i++) {
    output = "";
    if (i%3 === 0) {
      output += "Fizz";
    }
    if (i%5 === 0) {
      output += "Buzz";
    }
    if (output === "") {
      output = i;
    }
    console.log(output);
  }    
}

/**
 *
 * Prompts user for a beginning number.  Prints the numbers inclusively to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
 *
 */ 

const readline = require('readline');

function fizzbuzz_prompt() {

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  /*prompt("Enter FizzBuzz beginning number: ");
  var beg = readline();*/

  rl.question('Enter FizzBuzz beginning number: ', (beg) => {

    rl.close();
    
    var output;
    
    for(var i=beg;i<=100;i++) {
      output = "";
      if (i%3 === 0) {
        output += "Fizz";
      }
      if (i%5 === 0) {
        output += "Buzz";
      }
      if (output === "") {
        output = i;
      }
      console.log(output);
    }
  });
}
 
 fizzbuzz_prompt();
