//[level 0] 특이한 정렬 120880
//https://school.programmers.co.kr/learn/courses/30/lessons/120880

//결과 
//정확성: 100.0
//합계: 100.0 / 100.0

function solution(numlist, n) {
    return numlist.sort((a, b) => {
        //절댓값이 같은 경우 더 큰 값을 앞에다 두기
        if (Math.abs(a - n) === Math.abs(b - n)) 
            return a < b ? 1 : -1;
        //절댓값 차이를 기준으로 오름차순 정렬
        return Math.abs(a - n) - Math.abs(b - n)
    })
}