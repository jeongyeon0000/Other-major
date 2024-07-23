영어1,수학1,컴시일1 = map(float,input("1학기의 영어, 수학, 컴시일의 점수를 입력해주세요. ").split())
영어2,수학2,컴시일2 = map(float,input("2학기의 영어, 수학, 컴시일의 점수를 입력해주세요. ").split())
total1 = (영어1+수학1+컴시일1)/3
total2 = (영어2+수학2+컴시일2)/3
if total2 > total1:
    print("축하드립니다! 저번 시험보다 점수가", total2-total1,"만큼 오르셨습니다!")
elif total2 == total1:
    print("저번 시험과 "+str(total2)+"점으로 동일합니다.")
else:
    print("안타깝습니다..저번 시험보다 평균 점수가", total1-total2,"만큼 떨어지셨습니다..")