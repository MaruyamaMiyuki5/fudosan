# 必要なライブラリをインポート
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_profit(area, property_type, size, years_old):
    # この関数内で不動産の価値や運用益を計算するロジックを実装
    # ここでは簡単な例としてランダムな価値を返すようにしています
    return np.random.randint(100000, 1000000), np.random.randint(1000, 10000)

def main():
    st.title("不動産価値査定アプリ")
    
    # 入力を受け取る
    postal_code = st.text_input("物件の郵便番号を入力してください")
    property_type = st.selectbox("物件の種類を選択", ["一戸建て", "マンション・アパート", "土地"])
    size = st.number_input("専有面積を入力（㎡）", value=0.0)
    years_old = st.number_input("築年数を入力", value=0)
    
    if st.button("計算"):
        sale_value, monthly_profit = calculate_profit(postal_code, property_type, size, years_old)
        
        st.write(f"一括売却の金額: {sale_value}円")
        st.write(f"月々の運用益: {monthly_profit}円")
        
        years = list(range(1, 21))
        profits = [monthly_profit * 12 * year for year in years]
        
        plt.plot(years, profits, label="運用利益")
        plt.axhline(y=sale_value, color='r', linestyle='-', label="売却価格")
        plt.xlabel("運用年数")
        plt.ylabel("利益")
        plt.legend()
        
        st.pyplot(plt)

if __name__ == "__main__":
    main()

# 判断


#添付のWebアプリをstreamlitで作成するコードを教えてほしい。
#自分の持つ不動産価値を査定し、運用したほうが利益が出るのか
#売却したほうが良いのかを判断するアプリである。
#物件のエリアを郵便番号、物件の種類を（一戸建て、マンション・アパート、土地）をプルダウンで選択、専有面積を数値で、築年数を数値で入力し、月々の運用益を算出。
#一括売却の金額をもとに、売却が利益が高いのか、運用なら何年以上運用したら利益が高いのかをグラフ化してシュミレーションし、判断結果を回答する。