import streamlit as st

# Footer explanation about the ResNet-50 model
st.title("About the ResNet-50 Model")
st.write("""
The classification model used in this application is based on ResNet-50, a deep convolutional neural network architecture widely used in image classification tasks. ResNet-50 is a powerful model pre-trained on ImageNet, which has been fine-tuned on chess piece images to accurately identify different types of pieces.
""")

st.markdown("---")
st.subheader("Best-Model Results: Epoch 7")
st.image("./image/epoch.png")
st.write("The best model achieved an accuracy of 95.01% on the test dataset at Epoch 7, where early stopping was applied to prevent overfitting.")

st.markdown("---")
st.subheader("Heatmap of ResNet-50 Model ")
st.image("./image/heatmap.png")
st.write("The confusion matrix displays the model's performance on a test dataset at Epoch 7, where early stopping was applied to prevent overfitting.")

st.write("""
    ### Breakdown of Results:
    - **Bishop**: 5 true Bishops were correctly classified, with no misclassifications.
    - **King**: 7 true Kings were classified correctly, with 1 misclassified as Bishop.
    - **Knight**: 9 true Knights were correctly classified, with no misclassifications.
    - **Pawn**: 11 true Pawns were correctly classified, but 1 was misclassified as Rook.
    - **Queen**: 7 true Queens were correctly classified, with no misclassifications.
    - **Rook**: 14 true Rooks were correctly classified, with no misclassifications.
    """)

    # Overall Observations
st.write("""
    ### Overall Observations:
    - The model performs well in classifying most pieces, with minimal misclassifications.
    - There's a small misclassification issue for **Kings (1 misclassified as Bishop)** and **Pawns (1 misclassified as Rook)**.
    - Early stopping at Epoch 7 might indicate that the model reached an optimal point in terms of balancing accuracy and preventing overfitting. Further training could have led to overfitting, where performance on unseen data might have worsened.
    """)

st.markdown("---")
st.subheader("Graph Loss and Accuracy")
st.image("./image/graph.png")
st.write("""
    ### Interpretation of Loss and Accuracy Plots:
    - **Loss Log**: The training and validation loss dropped sharply after the first epoch and stabilized around zero in subsequent epochs. This indicates that the model quickly learned to fit the data and avoided further loss after initial training stages.
    - **Accuracy Log**: 
      - **Training Accuracy**: Increased steadily, reaching nearly 100% by the end of training, indicating that the model fit the training data well.
      - **Validation Accuracy**: Fluctuated across epochs, showing variations between 60% and 90%. This suggests some level of overfitting, as the model occasionally performs less consistently on validation data compared to the training data.
    """)

    # Observations Section
st.write("""
    ### Key Observations:
    - The **sharp initial drop in loss** and **rapid increase in accuracy** suggest that the model learned quickly during the early epochs.
    - **Validation accuracy fluctuation** indicates the model may be slightly overfitting to the training data, which aligns with the use of early stopping (observed from the confusion matrix plot at Epoch 7).
    - Potential overfitting can be addressed by using regularization techniques, dropout layers, or further tuning of training hyperparameters.
    """)