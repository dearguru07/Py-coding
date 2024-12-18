// var a=20
// function c(){
//     console.log('Hello world...')
// }
// // console.log(a)
// c()
// console.log(a)



// function fetchData(callback) {
//   setTimeout(() => {
//     const data = { name: "John", age: 30 };
//     callback(data);
//   }, 1000);
// }

// fetchData((data) => {
//   console.log(data); 
// });


function fetchData() {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        const data = { name: 'John', age: 30 };
        resolve(data);
      }, 1000);
    });
  }
  
  fetchData().then((data) => {
    console.log(data); // { name: 'John', age: 30 }
  }).catch((error) => {
    console.error(error);
  });
  