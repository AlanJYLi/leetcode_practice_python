Name: Jingyu Li (jli3006, 903520148)
Email: alanli@gatech.edu
EvalAI ID: alanjingyuli
EvalAI Email: alanli@gatech.edu
Leaderboard Name: alanjyli
Best Acc on EvalAI: 0.83

Final model: VGG-C with batch normalization and dropout

I followed the paper "VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION" and used a modified VGG-C ConvNet. My CNN included 13 conv-layers and 2 fc-layers. In each conv-layer, I only increased the number of channels and kept the size of output the same, e.g. (N, input_channels, h, w) to (N, output_channels, h, w).

Let's define conv(k,c) means convolution kernel with size k*k and c channels. And fc(n) means full connected layer with n output dimensions. Then the architecture is:
conv(3,64)-conv(3,64)-maxpooling(2,2)-conv(3,128)-conv(3,128)-maxpooling(2,2)-conv(3,256)-conv(3,256)-conv(1,256)-maxpooling(2,2)-conv(3,512)-conv(3,512)-conv(1,512)-maxpooling(2,2)-conv(3,512)-conv(3,512)-conv(1,512)-maxpooling(2,2)-flatten()-fc(1024)-fc(256)-fc(10)-softmax

My modification upon VGG-C mainly focused on the fc-layers. Since the picture size is relatively small, I decreased the number of neurons in each fc-layer and removed one fc-layer compared with original VGG-C.

To decrease overfitting, I added batch normalization operation after activation of each conv-layers. I also applied dropout with p=0.5 on the conv-layers with maxpooling and on the fc-layers.

I used SGD optimizer and the hyperparameters of my model are: epochs=30, weight-decay=0.00002, momentum=0.9, batch-size=64, lr=0.008.

Besides, I also set learning rate to reduce when the val_loss has stopped decreasing when training the model. In detail, I used torch.optim.lr_scheduler.ReduceLROnPlateau to adjust the learning rate based on the change of val_loss.

Other models I tried: VGG-A(11 layers), VGG-B(13 layers), VGG-C without dropout
