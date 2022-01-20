// 별찍기 2
//*
//***
//*****
//*******
//*********

let ch = ''
for(let i = 0; i < 5; i++){
    for(let i = 0; i < i*2+1 ; i++)
        {
            ch += '*'
        }
    ch += '\n'
}
console.log(ch)