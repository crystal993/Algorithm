//배열
let 광어들 = [50,100,150,200]

function 가격측정(물고기) {
    for(let i = 0 ; i < 물고기.length ; i++) {
        console.log((i+1)+"번째의 가격:"+물고기[i])
    }
}

console.log(가격측정(광어들))