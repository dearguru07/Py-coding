// "use Strict";
// x=20
// console.log(x)


const all=[1,5,'guru','charan','75',44,75,68]
const strs=[]
const values=[]

const res=all.forEach((x)=>{
    if(typeof(x)==='string'){
        strs.push(x)
    }
    else{
        values.push(x)
    }

})
console.log(strs)
console.log(values)