# Task of semantic relation classification

BÀI TẬP ĐO NHẬN DIỆN QUAN HỆ BAO THUỘC (HYPERNYMY) DỰA TRÊN WORD EMBEDDINGS VÀ KỸ THUẬT PHÂN LỚP CÓ GIÁM SÁT (SUPERVISED CLASSIFICATION) ) 

Sinh viên đăng ký chọn project theo một trong ba mức sau:
STANDARD
Viết chương phân lớp nhị phân có giám sát sử dụng support vector machine, pre-trained word embeddings (thư mục word2vec),
huấn luyện và đánh giá trên bộ dữ liệu VLE999 (thư mục Datasets).

MEDIUM
-  Viết chương phân lớp nhị phân có giám sát (sử dụng: logistic regression, multi-layer perceptron neural network, convolutional neural network...)
sử dụng pre-trained word embeddings (thư mục word2vec), huấn luyện và đánh giá trên bộ dữ liệu VLE999 (thư mục Datasets).

HARD
- Sử dụng WordNet làm mạnh thêm quan hệ Hypernymy của không gian Word Embeddings qua đó làm tăng hiệu quả phân lớp của 
kỹ thuật phân lớp có giám sát. (tham khảo: Specialising Word Vectors for Lexical Entailment, Ivan Vulic´ and Nikola Mrkšic´, 2017)
- Khai thác thông tin k từ gần nghĩa của từ để làm tăng hiệu quả phân lớp quan hệ. Để xác định quan hệ cho cặp từ (u,v), tìm k từ gần nghĩa
với u (cloud Su), và k từ gần nghĩa với v (cloud Sv)), khai thác quan hệ giữa các cặp từ giữa 2 cloud.
