let store = {
  state: {
    modules: [
      {
        "name": "scratchGui",
        "href": "/modules/scratchGui/index.html",
        "title": "스크래치 3 머신러닝",
        "license": "MIT",
        "description": "스크래치 3에 머신러닝 라이브러리를 추가한 애플리케이션입니다. 머신러닝의 기능들이 블록 형태로 구성되어 있어서 기존의 스크래치 블록과 유사하게 사용할 수 있습니다.",
        "source": "https://github.com/LLK/scratch-gui",
        "howTo": "일반적인 사용 방법은 스크래치 3와 동일합니다. 오른쪽 하단에 위치한 확장 기능 추가하기 버튼을 통해 확장 기능 블록 모음을 추가하여 사용합니다. 대표적으로, 손, 얼굴, 포즈 인식 기능이 있으며, 티처블 머신에서 제작한 모델을 가져와 사용할 수도 있습니다. ML2Scratch 기능을 이용하면 머신러닝 학습도 가능합니다.",
        "bookChapter": "실습",
        "bookPage": "85",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "スクラッチ 3 機械学習",
            "description": "スクラッチ 3 に機械学習ライブラリを追加したアプリケーションです",
            "howTo": "一般的な使い方は、スクラッチ3と同じです。 「Blue Machineで作成したモデルをインポートして使用することもできます。"
          },
          "en": {
            "title": "Scratch 3 Machine Learning",
            "description": "This is an application that adds a machine learning library to Scratch 3. Machine learning functions are organized in the form of blocks, so they can be used similarly to existing Scratch blocks.",
            "howTo": "The general method of use is the same as Scratch 3. Use the Add extension function button located at the bottom right to add a collection of extension function blocks. Representative examples include hand, face, and pose recognition functions, and the Teacher You can also import and use models created by Blue Machine. Machine learning learning is also possible using the ML2Scratch function."
          }
        }
      },
      {
        "name": "dqnRobot",
        "href": "/modules/dqnRobot/index.html",
        "title": "DQN 자동차",
        "license": "None",
        "description": "DQN 기반의 자율주행 자동차 시뮬레이터입니다. 이 시뮬레이터는 DQN을 활용하여 자동차가 스스로 주행하는 방법을 학습합니다.",
        "source": "https://github.com/leetenki/dqnRobot",
        "howTo": "자동차는 스스로 학습하기 때문에 별도의 조작은 필요하지 않습니다. 30분 이상 충분히 학습을 진행한 후에는 위쪽에 위치한 둥근 노란색 버튼을 눌러 자유 주행 모드로 전환해보세요. 이제 자동차는 코스를 정확하게 주행할 것입니다. 왼쪽 메뉴를 통해 차량이나 큐브 등을 추가, 제거하거나 이미 훈련된 차량을 가져올 수 있습니다.",
        "bookChapter": "DQN, 게임, 자율주행, 학습",
        "bookPage": "14, 98",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "DQN車",
            "description": "DQN ベースの自律走行車シミュレータです。このシミュレータは、DQN を活用して車が自分で走行する方法を学習します。",
            "howTo": "自動車は自分で学習するので、別途の操作は必要ありません。走行します。左側のメニューから車両やキューブなどを追加、削除したり、既に訓練された車両をインポートしたりできます。"
          },
          "en": {
            "title": "DQN Car",
            "description": "A DQN-based self-driving car simulator. This simulator leverages DQN to help cars learn how to drive themselves.",
            "howTo": "The car learns on its own, so no separate operation is required. After learning for more than 30 minutes, press the round yellow button at the top to switch to free driving mode. The car will now accurately follow the course. You can add or remove vehicles, cubes, etc. or import already trained vehicles through the menu on the left."
          }
        }
      },
      {
        "name": "defrosting",
        "href": "/modules/mediaPipe/mediapipeice-defrosting-demo-effect/index.html",
        "title": "Defrosting (서리 제거)",
        "license": "Apache License 2.0",
        "description": "카메라로 촬영되는 영상에 서리가 끼는 것을 제거하는 게임입니다. 이 게임은 손 인식 모델을 활용하여 제작되었습니다.",
        "source": "https://codepen.io/mediapipe/pen/bGweWyR",
        "howTo": "가만히 있으면 촬영 중인 영상에 서리가 끼게 됩니다. 화면에 손을 보이게 하고 움직이면 손이 지나간 부분의 서리만 사라집니다. 한 번에 하나의 손만 인식되며, 시간이 지나면 사라졌던 서리가 다시 나타납니다.",
        "bookChapter": "인식, 재미",
        "bookPage": "75",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "Defrosting (霜の除去)",
            "description": "カメラで撮影された映像に霜が付くのを除去するゲームです。このゲームは手認識モデルを活用して制作されました。",
            "howTo": "静かにすると撮影中の映像に霜が挟み込まれます。 画面に手を見せて動かすと手が通った部分の霜だけ消えます。"
          },
          "en": {
            "title": "Defrosting",
            "description": "This is a game that removes frost from images captured by a camera. The game was created using a hand recognition model.",
            "howTo": "If you stay still, frost will appear on the video you are shooting. If you make your hand visible on the screen and move it, only the part where your hand passed will disappear. Only one hand will be recognized at a time, and after some time, the frost will appear again. It flies."
          }
        }
      },
      {
        "name": "objectron",
        "href": "/modules/mediaPipe/mediapipeobjectron/index.html",
        "title": "Objectron (3D 객체)",
        "license": "Apache License 2.0",
        "description": "이 애플리케이션은 일상에서 흔히 볼 수 있는 물체를 3D로 인식할 수 있습니다. 특정 데이터로 학습된 사물에 대해 실시간으로 포즈를 추정하여 보여줍니다.",
        "source": "https://codepen.io/mediapipe/pen/BaWvzdY",
        "howTo": "왼쪽의 메뉴에서 인식하고자 하는 사물을 모델 메뉴에서 선택하세요. 인식 가능한 사물은 신발, 카메라, 의자, 컵입니다. 그 다음, 카메라 앞에 사물을 가져와주세요. 사물이 인식되면 화면에 사물의 테두리와 XYZ 축이 표시됩니다.",
        "bookChapter": "인식, 물체",
        "bookPage": "74",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "Objectron (3D オブジェクト)",
            "description": "このアプリケーションは、日常的によく見られるオブジェクトを3Dとして認識することができます。",
            "howTo": "左側のメニューから認識したいものをモデルメニューから選択してください。認識可能なものは靴、カメラ、椅子、カップです。その後、カメラの前に物を持ってきてください。の枠線とXYZ軸が表示されます。"
          },
          "en": {
            "title": "Objectron (3D object)",
            "description": "This application can recognize objects commonly seen in everyday life in 3D. It estimates and displays the pose of objects learned with specific data in real time.",
            "howTo": "Select the object you want to recognize from the model menu in the menu on the left. Objects that can be recognized include shoes, cameras, chairs, and cups. Then, bring the object in front of the camera. Once the object is recognized, it will appear on the screen. The borders and XYZ axes are displayed."
          }
        }
      },
      {
        "name": "hands",
        "href": "/modules/mediaPipe/mediapipehands/index.html",
        "title": "Hands (손)",
        "license": "Apache License 2.0",
        "description": "MediaPipe는 손과 손가락을 추적할 수 있는 솔루션을 제공합니다. 1-4개의 손에서 21개 주요 부분의 움직임을 추적할 수 있습니다.",
        "source": "https://codepen.io/mediapipe/pen/RwGWYJw",
        "howTo": "카메라에 손이 보이게 하면 손의 주요 부분이 점과 선으로 표시됩니다. 각 손은 다른 색으로 표시되며, 왼쪽 메뉴에서 최대 손의 숫자를 1~4개까지 변경할 수 있습니다.",
        "bookChapter": "인식, 손",
        "bookPage": "62",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "Hands (手)",
            "description": "MediaPipeは手と指を追跡するためのソリューションを提供します。1〜4つの手で21の主要部分の動きを追跡できます。",
            "howTo": "カメラに手が見えるようにすると、手の主要部分が点と線で表示されます。各手は異なる色で表示され、左メニューから最大手の数字を1～4個まで変更できます。"
          },
          "en": {
            "title": "Hands",
            "description": "MediaPipe provides a solution for hand and finger tracking. It can track the movements of 21 key parts in 1-4 hands.",
            "howTo": "When you make a hand visible to the camera, the main parts of the hand are displayed as dots and lines. Each hand is displayed in a different color, and you can change the maximum number of hands from 1 to 4 in the menu on the left."
          }
        }
      },
      {
        "name": "faceMesh",
        "href": "/modules/mediaPipe/mediapipeface-mesh/index.html",
        "title": "Face Mesh (얼굴 그물)",
        "license": "Apache License 2.0",
        "description": "MediaPipe는 얼굴 인식 솔루션을 제공합니다. 얼굴의 468개 지점을 추정하고 3D 형태로 변환하여 얼굴에 맞춰 보여줍니다.",
        "source": "https://codepen.io/mediapipe/pen/KKgVaPJ",
        "howTo": "화면에 얼굴을 비추면 얼굴의 주요 부분이 선과 그물 형태로 표시됩니다. 왼쪽 메뉴에서 최대 얼굴 숫자를 1~4개까지 변경할 수 있습니다.",
        "bookChapter": "인식, 얼굴",
        "bookPage": "60",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "Face Mesh (顔ネット)",
            "description": "MediaPipe は顔認識ソリューションを提供します。顔の 468 点を推定し、3D 形式に変換して顔に合わせて表示します。",
            "howTo": "画面に顔を照らすと、顔の主な部分が線と網の形で表示されます。左メニューから最大顔数を1〜4個まで変更できます。"
          },
          "en": {
            "title": "Face Mesh",
            "description": "MediaPipe provides a facial recognition solution. It estimates 468 points on the face and converts them into a 3D shape to fit the face.",
            "howTo": "When you show a face on the screen, the main parts of the face are displayed in the form of lines and meshes. You can change the maximum number of faces from 1 to 4 in the menu on the left."
          }
        }
      },
      {
        "name": "pose",
        "href": "/modules/mediaPipe/mediapipepose/index.html",
        "title": "Pose (포즈)",
        "license": "Apache License 2.0",
        "description": "MediaPipe는 포즈 인식 솔루션을 제공합니다. 사람 몸 전체에서 33개 주요 부분의 위치를 추정하고 이들을 연결해서 뼈대와 같이 보여줍니다.",
        "source": "https://codepen.io/mediapipe/pen/jOMbvxw",
        "howTo": "화면에 몸을 비추면 주요 부분이 뼈대로 연결되어 표시됩니다. 화면의 오른쪽에는 인식된 주요 부위가 선과 점으로 표현됩니다.",
        "bookChapter": "인식, 자세",
        "bookPage": "61",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "Pose (ポーズ)",
            "description": "MediaPipe はポーズ認識ソリューションを提供します。人体全体で 33 の主要部分の位置を推定し、それらを連結してスケルトンのように見せます。",
            "howTo": "画面に体を照らすと、主要部分が骨格でつながって表示されます。画面右側には、認識された主要部位が線と点で表されます。"
          },
          "en": {
            "title": "Pose",
            "description": "MediaPipe provides a pose recognition solution. It estimates the positions of 33 major parts of the entire human body and connects them to display them like a skeleton.",
            "howTo": "When you show your body on the screen, the main parts are displayed as a skeleton. On the right side of the screen, the recognized main parts are represented by lines and dots."
          }
        }
      },
      {
        "name": "holistic",
        "href": "/modules/mediaPipe/mediapipeholistic/index.html",
        "title": "Holistic (전체적)",
        "license": "Apache License 2.0",
        "description": "MediaPipe의 손, 얼굴 그물, 포즈의 기능들을 통합하여 제공합니다.",
        "source": "https://codepen.io/mediapipe/pen/LYRRYEw",
        "howTo": "화면에 전신을 비추면 얼굴 그물, 손, 포즈 기능이 모두 적용되어 표시됩니다.",
        "bookChapter": "인식, 자세",
        "bookPage": "63",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "Holistic (全体)",
            "description": "MediaPipe の手、フェイスネット、ポーズの機能を統合して提供します。",
            "howTo": "画面に全身を当てると、顔ネット、手、ポーズ機能がすべて適用されて表示されます。"
          },
          "en": {
            "title": "Holistic",
            "description": "Integrates MediaPipe's hand, face net, and pose features.",
            "howTo": "When your whole body is on the screen, the face mesh, hands, and pose features are all applied and displayed."
          }
        }
      },
      {
        "name": "faceDetection",
        "href": "/modules/mediaPipe/mediapipeface-detection/index.html",
        "title": "Face Detection (얼굴 인식)",
        "license": "Apache License 2.0",
        "description": "MediaPipe의 얼굴 인식 솔루션은 얼굴의 유무를 빠르게 감지하고, 6개의 주요 부분을 표시해줍니다. 이 기능은 간단해서 처리 속도가 매우 빠릅니다.",
        "source": "https://codepen.io/mediapipe/pen/dyOzvZM",
        "howTo": "화면에 얼굴을 비추면 얼굴 전체가 사각형으로, 주요 부위가 점으로 표시됩니다.",
        "bookChapter": "인식, 얼굴",
        "bookPage": "59",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "Face Detection (顔認識)",
            "description": "MediaPipeの顔認識ソリューションは、顔の有無をすばやく検出し、6つの主要部分を表示します。この機能は簡単で処理速度が非常に高速です。",
            "howTo": "画面に顔を照らすと、顔全体が四角形になり、主要部位が点として表示されます。"
          },
          "en": {
            "title": "Face Detection",
            "description": "MediaPipe's facial recognition solution quickly detects the presence or absence of a face and displays six key parts. The functionality is simple and the processing speed is very fast.",
            "howTo": "When you show your face on the screen, the entire face is displayed as a square, with key areas displayed as dots."
          }
        }
      },
      {
        "name": "segmentation",
        "href": "/modules/mediaPipe/mediapipeselfie-segmentation/index.html",
        "title": "Selfie Segmentation (셀카 분할)",
        "license": "Apache License 2.0",
        "description": "실시간 영상에서 사람을 제거하거나 배경을 제거할 수 있는 MediaPipe의 솔루션입니다. 이 기능은 영상 합성 등에 활용될 수 있습니다.",
        "source": "https://codepen.io/mediapipe/pen/wvJyQpq",
        "howTo": "화면 왼쪽의 메뉴에서 효과를 전경으로 설정하면 사람만 초록색으로 표시되고, 배경으로 설정하면 배경만 파란색으로 표시됩니다.",
        "bookChapter": "인식, 배경 분리",
        "bookPage": "",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "Selfie Segmentation (自分撮り分割)",
            "description": "リアルタイム映像から人を削除したり、背景を削除したりできるMediaPipeのソリューションです。この機能は映像合成などに活用できます。",
            "howTo": "画面左側のメニューでエフェクトを前景に設定すると、人だけが緑色で表示され、背景に設定すると背景のみ青で表示されます。"
          },
          "en": {
            "title": "Selfie Segmentation",
            "description": "MediaPipe's solution for removing people or backgrounds from real-time video. This feature can be used for video compositing, etc.",
            "howTo": "If you set the effect to foreground from the menu on the left side of the screen, only the person will appear green. If you set it to background, only the background will appear blue."
          }
        }
      },
      {
        "name": "faceApi",
        "href": "/modules/faceApi/index.html",
        "title": "Face-API",
        "license": "MIT",
        "description": "TensorFlow를 이용하여 만든 얼굴 인식 앱입니다. 이 앱은 인식된 얼굴에서 표정과 나이 등의 정보를 추측하여 보여줍니다.",
        "source": "https://github.com/justadudewhohacks/face-api.js",
        "howTo": "화면 왼쪽에서 원하는 메뉴를 선택할 수 있습니다. 모든 메뉴는 얼굴과 관련되어 있으며, 파란색 상자 위의 숫자는 얼굴 신뢰도를 나타냅니다. (숫자 1은 100%를 의미합니다.) 메뉴 이름 앞에 웹캠이 붙은 것은 웹캠이 필요한 기능입니다. 얼굴 자체 인식과 더불어 랜드마크, 표정, 연령 및 성별 인식을 사용해 볼 수 있습니다.",
        "bookChapter": "인식, 구분, 표정, 영상",
        "bookPage": "66",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "Face-API",
            "description": "TensorFlowを使用して作成した顔認識アプリです。このアプリは、認識された顔から表情や年齢などの情報を推測して表示します。",
            "howTo": "画面の左側から目的のメニューを選択できます。すべてのメニューは顔に関連付けられており、青いボックスの上の数字は顔の信頼性を表します（数字1は100％を意味します。）メニュー名の前にウェブカメラが付いているのはウェブカメラが必要な機能です"
          },
          "en": {
            "title": "Face-API",
            "description": "This is a face recognition app created using TensorFlow. This app guesses and displays information such as expression and age from the recognized face.",
            "howTo": "You can select the desired menu on the left side of the screen. All menus are related to faces, the number above the blue box indicates the face confidence (the number 1 means 100%) before the menu name. It's a feature that requires a webcam. In addition to self-recognition of the face, you can try using landmarks, facial expressions, age and gender recognition."
          }
        }
      },
      {
        "name": "disappearingPeople",
        "href": "/modules/disappearingPeople/index.html",
        "title": "움직이는 사람 지우기",
        "license": "Apache License 2.0",
        "description": "TensorFlow를 이용하여 실시간으로 배경에서 사람을 제거하는 기능을 제공합니다. 이 기능은 사람을 인식하고 배경을 학습하는 과정을 통해 장면에서 사람을 제거합니다.",
        "source": "https://github.com/jasonmayes/Real-Time-Person-Removal",
        "howTo": "페이지 하단에 있는 웹캠 활성화 버튼을 클릭하면 2개의 영상이 나옵니다. 위쪽은 웹캠으로 찍은 원본 영상이고, 아래쪽은 사람이 지워진 영상입니다. 웹캠 촬영 범위를 넘나들면 아래쪽 영상에서 사람이 점차 사라지는 것을 확인할 수 있습니다.",
        "bookChapter": "배경 분리, 영상",
        "bookPage": "",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "動く人をクリア",
            "description": "TensorFlowを使用して、リアルタイムで背景から人を削除する機能を提供します。この機能は、人を認識し、背景を学習する過程を通じてシーンから人を削除します。",
            "howTo": "ページ下部にあるウェブカメラを有効にする」ボタンをクリックすると、2つの映像が出ます。消えることを確認できます。"
          },
          "en": {
            "title": "Erase movers",
            "description": "Provides a feature to remove people from the background in real time using TensorFlow. This feature recognizes people and removes them from a scene through the process of learning the background.",
            "howTo": "When you click the webcam activation button at the bottom of the page, two images will appear. The upper image is the original image taken by the webcam, and the lower image is the image with the person removed. As you move beyond the webcam shooting range, the person gradually appears in the lower image. You can see it disappearing."
          }
        }
      },
      {
        "name": "poseAnimatorStatic",
        "href": "/modules/poseAnimator/static_index.html",
        "title": "포즈 애니메이터 (사진)",
        "license": "Apache License 2.0",
        "description": "정지된 사진에서 얼굴과 포즈를 인식하고, 이를 이용해서 캐릭터 애니메이션을 만드는 앱입니다.",
        "source": "https://github.com/yemount/pose-animator",
        "howTo": "화면 왼쪽에는 얼굴과 포즈가 표시된 원본 사진이 보이고, 오른쪽에는 이를 반영한 캐릭터가 보입니다. 오른쪽 위의 메뉴에서 원본 이미지를 변경할 수 있고, 아바타 SVG로 캐릭터의 성별을 변경할 수 있습니다.",
        "bookChapter": "인식, 자세, 재미",
        "bookPage": "",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "ポーズアニメーター(写真)",
            "description": "静止画で顔やポーズを認識し、それを利用してキャラクターアニメーションを作成するアプリです。",
            "howTo": "画面の左側には顔とポーズが表示された元の写真が表示され、右側にはこれを反映したキャラクターが表示されます。右上のメニューから元の画像を変更でき、アバターSVGでキャラクターの性別を変更できます。"
          },
          "en": {
            "title": "Pose Animator (Photo)",
            "description": "This is an app that recognizes faces and poses from still photos and uses them to create character animations.",
            "howTo": "On the left side of the screen you will see the original photo with the face and pose, and on the right you will see a reflection of the character. You can change the original image in the menu at the top right, and change the character's gender with the avatar SVG."
          }
        }
      },
      {
        "name": "poseAnimatorCamera",
        "href": "/modules/poseAnimator/camera_index.html",
        "title": "포즈 애니메이터 (웹캠)",
        "license": "Apache License 2.0",
        "description": "촬영한 영상에서 실시간으로 사람의 포즈와 얼굴을 인식하고, 이를 움직이는 캐릭터 애니메이션으로 만드는 앱입니다.",
        "source": "https://github.com/yemount/pose-animator",
        "howTo": "화면 왼쪽 위에는 얼굴과 포즈가 표시된 영상이 나오고, 화면 중앙에는 이를 반영한 캐릭터가 나옵니다. 얼굴과 몸을 움직이면 캐릭터도 따라 움직입니다. 오른쪽 위의 아바타 SVG로 캐릭터의 성별을 변경할 수 있습니다.",
        "bookChapter": "인식, 자세, 재미",
        "bookPage": "75",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "ポーズアニメーター(ウェブカメラ)",
            "description": "撮影した映像でリアルタイムで人のポーズや顔を認識し、これを動かすキャラクターアニメーションにするアプリです。",
            "howTo": "画面左上には顔とポーズが表示された映像が出て、画面中央にはこれを反映したキャラクターが出てきます。顔や体を動かすとキャラクターも動きます。"
          },
          "en": {
            "title": "Pose Animator (Webcam)",
            "description": "This is an app that recognizes people's poses and faces in real time from captured videos and turns them into moving character animations.",
            "howTo": "A video showing the face and pose appears in the top left of the screen, and a character reflecting this appears in the center of the screen. If you move your face and body, the character moves along. You can change the character's gender with the avatar SVG in the top right. ."
          }
        }
      },
      {
        "name": "kalidokit",
        "href": "/modules/kalidokit/live2d/index.html",
        "title": "애니메이션 모션 트래킹",
        "license": "MIT",
        "description": "MediaPipe와 TensorFlow를 이용하여 캐릭터 애니메이션을 만들 수 있습니다. 이 기능은 사람의 얼굴 또는 전체를 인식해서 캐릭터가 따라 움직이는 것을 구현하였습니다.",
        "source": "https://github.com/yeemachine/kalidokit",
        "howTo": "웹캠으로 사람을 비추면 사람의 포즈와 표정을 인식해서 움직이는 캐릭터 애니메이션을 출력해줍니다. 오른쪽 아래에서 Live2D를 선택하면 얼굴만, VRM을 선택하면 얼굴, 손, 몸 전체의 움직임을 반영한 캐릭터를 사용할 수 있습니다.",
        "bookChapter": "인식, 자세, 재미",
        "bookPage": "64",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "アニメーションモーショントラッキング",
            "description": "MediaPipeとTensorFlowを使ってキャラクターアニメーションを作成することができます。",
            "howTo": "ウェブカメラで人を照らすと人のポーズと表情を認識して動くキャラクターアニメーションを出力します。右下でLive2Dを選択すると顔だけ、VRMを選択すると顔、手、体全体の動きを反映した」キャラクターが使えます。"
          },
          "en": {
            "title": "Animation Motion Tracking",
            "description": "You can create character animations using MediaPipe and TensorFlow. This feature recognizes a person's face or the entire person and makes the character move along.",
            "howTo": "When you point a webcam at a person, it recognizes the person's pose and expression and outputs a moving character animation. If you select Live2D at the bottom right, only the face will be reflected, and if you select VRM, it will reflect the movements of the face, hands, and entire body. You can use the character."
          }
        }
      },
      {
        "name": "doodleRecognition",
        "href": "/modules/doodleRecognition/index.html",
        "title": "그림 인식",
        "license": "MIT",
        "description": "퀵드로우의 손 그림 데이터 세트를 학습하여 사용자의 그림이 무엇인지 인식하는 게임입니다. 이 게임은 CNN을 이용하여 그림을 학습하고 인식합니다.",
        "source": "https://github.com/ssusnic/Machine-Learning-Doodle-Recognition",
        "howTo": "화면 오른쪽 캔버스에 벌, 양초, 자동차, 시계, 기타, 문어, 눈사람, 나무, 우산 중 하나를 그려보세요. 그림을 그리면 캔버스 아래에 컴퓨터가 예상한 답이 출력됩니다. 인식률이 낮으면 더 훈련하기 버튼을 눌러서 추가 훈련을 시킬 수 있습니다. 추가 훈련을 시키면 예측 정확도가 올라갑니다.",
        "bookChapter": "그림, 인식, 학습, CNN",
        "bookPage": "15, 123",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "画像認識",
            "description": "クイックドローの手描きデータセットを学習し、ユーザーの絵が何であるかを認識するゲームです。このゲームはCNNを利用して絵を学習して認識します。",
            "howTo": "画面右側のキャンバスに蜂、キャンドル、車、時計、ギター、タコ、雪だるま、木、傘のいずれかを描いてみてください。絵を描くと、キャンバスの下にコンピュータが期待した答えが出力されます。認識率が低い「トレーニングを続ける」ボタンを押して追加のトレーニングを実行できます。追加のトレーニングを実行すると予測精度が上がります。"
          },
          "en": {
            "title": "Picture Recognition",
            "description": "This is a game that learns from QuickDraw's hand drawing dataset to recognize what the user's drawing is. The game uses CNN to learn and recognize drawings.",
            "howTo": "Draw a bee, a candle, a car, a clock, a guitar, an octopus, a snowman, a tree, or an umbrella on the canvas on the right side of the screen. When you draw, the computer's expected answer is displayed below the canvas. Recognition rate is low. If so, you can perform additional training by clicking the Train More button. If you perform additional training, the prediction accuracy will increase."
          }
        }
      },
      {
        "name": "sketcher",
        "href": "/modules/sketcher/index.html",
        "title": "스캐쳐 (그림 인식)",
        "license": "None",
        "description": "CNN을 이용하여 퀵드로우의 손 그림 데이터를 학습하고 학습한 그림을 인식하는 앱입니다. 이 앱은 100개의 그림을 인식할 수 있습니다.",
        "source": "https://github.com/zaidalyafeai/zaidalyafeai.github.io/tree/master/sketcher",
        "howTo": "화면 아래에 있는 100개의 학습 목록 중 하나를 화면 왼쪽 캔버스에 그려 보세요. 화면 오른쪽에 그림과 일치할 확률이 높은 상위 5개의 결과가 수치와 함께 표시됩니다.",
        "bookChapter": "그림, 인식, CNN",
        "bookPage": "17",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "スキャッチャー (画像認識)",
            "description": "CNNを利用してクイックドローの手描きデータを学習し、学習した絵を認識するアプリです。このアプリは100個の絵を認識できます。",
            "howTo": "画面の下にある100個の学習リストの1つを画面の左側のキャンバスに描きます。"
          },
          "en": {
            "title": "Scatcher (Picture Recognition)",
            "description": "This is an app that uses CNN to learn QuickDraw's hand drawing data and recognize the learned drawings. This app can recognize 100 drawings.",
            "howTo": "Draw one of the 100 learning lists at the bottom of the screen on the canvas on the left side of the screen. The top five results most likely to match the drawing are displayed with numbers on the right side of the screen."
          }
        }
      },
      {
        "name": "quickdraw",
        "href": "https://quickdraw.withgoogle.com",
        "title": "퀵 드로우",
        "license": "External Site",
        "description": "사용자가 문제로 제시한 그림을 그리면 그 그림이 무엇인지 학습된 인공지능이 맞추는 게임입니다.",
        "source": "https://quickdraw.withgoogle.com",
        "howTo": "한 게임 당 6개의 라운드로 구성되어 있습니다. 각 라운드마다 제시된 사물을 그림으로 그리면 인공지능이 반복해서 답을 예측하게 됩니다. 인공지능이 답을 맞추면 다음 라운드로 넘어갈 수 있습니다.",
        "bookChapter": "그림, 인식, 재미, CNN",
        "bookPage": "127",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "クイックドロー",
            "description": "ユーザーが問題として提示した絵を描くと、その絵が何なのか学習された人工知能が合うゲームです。",
            "howTo": "ゲームごとに6つのラウンドで構成されています。各ラウンドごとに提示されたものを絵で描くと、人工知能が繰り返し答えを予測することになります。人工知能が答えを合わせれば次のラウンドに進むことができます。"
          },
          "en": {
            "title": "Quick Draw",
            "description": "This is a game where the user draws a picture presented as a problem and the learned artificial intelligence guesses what the picture is.",
            "howTo": "One game consists of six rounds. In each round, you draw a picture of the presented object and the artificial intelligence repeatedly predicts the answer. If the artificial intelligence guesses the answer, you can move on to the next round."
          }
        }
      },
      {
        "name": "autodraw",
        "href": "https://www.autodraw.com",
        "title": "오토 드로우",
        "license": "External Site",
        "description": "사용자가 그린 그림이 무엇인지 예측하고, 일치할 확률이 높은 아이콘들을 제시해서 사용자가 선택할 수 있도록 만든 그리기 앱입니다.",
        "source": "https://www.autodraw.com",
        "howTo": "왼쪽의 버튼들 중에서 AutoDraw를 선택하고 그림을 그려보세요. 그림과 비슷한 형태의 아이콘들이 화면 위에 표시될 것입니다. 이 중에서 하나를 선택하면 해당 아이콘으로 그림이 바뀝니다. 아이콘은 Fill 버튼으로 색칠이 가능합니다. Draw, Type, Shape 버튼으로 일반적인 형태의 그림들도 그릴 수 있습니다.",
        "bookChapter": "그림, 인식, CNN, 재미",
        "bookPage": "127",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "オートドロー",
            "description": "ユーザーが描いた絵が何であるかを予測し、一致する可能性が高いアイコンを提示してユーザーが選択できるようにした描画アプリです。",
            "howTo": "左のボタンの中からAutoDrawを選択して絵を描いてみてください。絵のような形のアイコンが画面の上に表示されます。この中から1つを選択すると、そのアイコンに絵が変わります。アイコンはFillボタンで塗りつぶすことができます。 Draw、Type、Shapeボタンで、一般的な形の絵も描くことができます。"
          },
          "en": {
            "title": "Auto Draw",
            "description": "This is a drawing app that predicts what the user has drawn and presents icons with a high probability of matching so that the user can select them.",
            "howTo": "Select AutoDraw from the buttons on the left and draw a picture. Icons similar to the picture will be displayed on the screen. If you select one of these, the picture will change to that icon. The icon is the Fill button. You can color with . You can also draw pictures in general shapes with the Draw, Type, and Shape buttons."
          }
        }
      },
      {
        "name": "magicSketchpad",
        "href": "/modules/magicSketchpad/index.html",
        "title": "자동 완성 그리기 (Magenta)",
        "license": "Apache License 2.0",
        "description": "RNN을 활용하여 만든 이어 그리기 앱입니다. 퀵드로우의 데이터 세트를 학습하여 사용자가 그림을 그리면 손 그림처럼 이어서 그려주는 기능을 가지고 있습니다.",
        "source": "https://glitch.com/edit/#!/magic-sketchpad",
        "howTo": "왼쪽 위에 cat이 선택되어 있는 선택 상자를 클릭하여 그리기를 원하는 사물을 고르세요. 그런 다음 캔버스에 해당 사물을 그리기 시작하면 나머지 부분을 인공지능이 이어서 그려줄 것입니다. 그림이 마음에 들지 않으면 선택 상자 왼쪽의 다시 그리기 버튼을 이용해서 새로 그림을 이어 그리게 할 수 있습니다.",
        "bookChapter": "그림, 인식, RNN, 재미",
        "bookPage": "37, 136",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "自動完成の描画 (Magenta)",
            "description": "RNNを活用して作成したイヤー描画アプリです。QuickDrawのデータセットを学習し、ユーザーが絵を描くと手描きのように引き継ぐ機能を持っています。",
            "howTo": "左上にcatが選択されている選択ボックスをクリックして描きたいものを選んでください。その後、キャンバスにそのものを描き始めると、残りの部分を人工知能が続いて描きます。そうでない場合は、選択ボックスの左側にある再描画ボタンを使用して、新しい絵を描き続けることができます。"
          },
          "en": {
            "title": "Draw Autocomplete (Magenta)",
            "description": "This is a continuous drawing app created using RNN. It learns the QuickDraw data set and has a function to continue drawing like a hand drawing when the user draws.",
            "howTo": "Click on the selection box with cat selected in the upper left corner to select the object you want to draw. Then, start drawing the object on the canvas and AI will draw the rest. Drawing is the mind. If it is not included, you can use the redraw button on the left of the selection box to draw a new picture."
          }
        }
      },
      {
        "name": "dodgeFallingBalls",
        "href": "/modules/dodgeFallingBalls/index.html",
        "title": "떨어지는 공 피하기 (DQN)",
        "license": "None",
        "description": "DQN을 활용하여 공 피하기 방법을 학습하는 과정을 보여주는 앱입니다. 에이전트는 센서로부터 정보를 받고 오래 살아 있을 수록 많은 보상을 받습니다.",
        "source": "https://github.com/seann999/dodge_tfjs",
        "howTo": "시작 버튼을 누르면 큐브가 좌우로 움직이며 공을 피하게 됩니다. 공에 맞으면 다음 라운드가 시작됩니다. 이 과정을 반복하면 점차 더 오래 생존할 수 있게 되며, 그 변화는 화면 아래의 그래프에서 확인할 수 있습니다. 수동 컨트롤을 체크하면 키보드 A와 D키로 수동 조종이 가능합니다.",
        "bookChapter": "DQN, 게임, 학습",
        "bookPage": "42, 103",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "落ちるボールを避ける (DQN)",
            "description": "DQN を活用して空避する方法を学習する過程を示すアプリです。 エージェントはセンサーから情報を受け取り、長く生きているほど多くの報酬を受けます。",
            "howTo": "スタートボタンを押すとキューブが左右に移動し、ボールを避けることができます。ボールに当たると次のラウンドが始まります。グラフで確認できます。手動コントロールをチェックすると、キーボードAとDキーで手動操作が可能です"
          },
          "en": {
            "title": "Avoid falling balls (DQN)",
            "description": "This is an app that demonstrates the process of learning how to avoid a ball using DQN. The agent receives information from sensors and receives more rewards the longer it stays alive.",
            "howTo": "Pressing the start button will make the cube move left and right to avoid the ball. If it gets hit by the ball, the next round will start. If you repeat this process, you will gradually be able to survive longer, and the changes are shown at the bottom of the screen. You can check it in the graph. If you check manual control, you can manually control it with the A and D keys on the keyboard."
          }
        }
      },
      {
        "name": "dqnBagel",
        "href": "/modules/dqnBagel/index.html",
        "title": "비행기 전쟁 (DQN)",
        "license": "None",
        "description": "DQN을 활용하여 적 비행기 피하기 학습 과정을 보여주는 앱입니다. 에이전트는 센서로부터 정보를 받고 오래 살아 있을 수록 많은 보상을 받습니다.",
        "source": "https://github.com/Maggie-29/dqnbagel",
        "howTo": "페이지를 아래로 내려서 시작 버튼을 누르면 비행기가 좌우로 움직이며 적 비행기를 피하게 됩니다. 총알은 일정 간격으로 계속 나와서 적 비행기를 파괴합니다. 우리 비행기가 파괴되면 새로운 라운드가 시작되며, 점차 더 오래 살아남게 됩니다. 수동 컨트롤을 체크하면 A와 D키로 수동 조종이 가능합니다.",
        "bookChapter": "DQN, 게임, 학습",
        "bookPage": "105",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "飛行機戦争 (DQN)",
            "description": "DQNを活用して敵飛行機を避ける学習過程を示すアプリです。エージェントはセンサーから情報を受け取り、長く生きているほど多くの報酬を受けます。",
            "howTo": "ページを下にしてスタートボタンを押すと、飛行機が左右に移動し、敵の飛行機を避けることができます。弾丸は一定間隔で継続して出て敵飛行機を破壊します。 、徐々に長く生き残ります。 手動コントロールをチェックすると、AとDキーで手動操縦が可能です"
          },
          "en": {
            "title": "Plane Wars (DQN)",
            "description": "This is an app that demonstrates the learning process of avoiding enemy planes using DQN. The agent receives information from sensors and the longer it stays alive, the more rewards it receives.",
            "howTo": "When you scroll down the page and press the start button, your plane will move left and right to avoid enemy planes. Bullets will keep coming out at regular intervals and destroy enemy planes. When our plane is destroyed, a new round will start and , you will gradually survive longer. If you check manual control, you can manually control it with the A and D keys."
          }
        }
      },
      {
        "name": "dqnCartpole",
        "href": "/modules/dqnCartpole/index.html",
        "title": "봉 균형 잡기",
        "license": "Apache License 2.0",
        "description": "TensorFlow를 이용하여 강화학습을 수행하는 과정을 보여주는 앱입니다. 이 과정의 목표는 가능한 오랜 시간 동안 봉의 균형을 잡는 것입니다.",
        "source": "https://github.com/tensorflow/tfjs-examples/tree/master/cart-pole",
        "howTo": "훈련 버튼을 누르면 봉을 쓰러뜨리지 않기 위한 게임이 시작됩니다. 이 게임은 20번의 게임과 가중치 업데이트 과정을 총 20번 반복합니다. 반복이 계속되면 점점 오랜 시간(스텝)동안 봉을 쓰러뜨리지 않게 될 것입니다. 반복 횟수 등과 같은 설정을 변경할 수도 있습니다.",
        "bookChapter": "게임, 학습",
        "bookPage": "",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "棒バランスをとる",
            "description": "TensorFlowを使用して強化学習を実行するプロセスを示すアプリ",
            "howTo": "訓練ボタンを押すと棒を倒さないためのゲームが始まります。 このゲームは20回のゲームと重み更新過程を合計20回繰り返す。繰り返しが続くとますます長い時間（ステップ）の間棒倒すことはありません。繰り返し回数などの設定を変更することもできます。"
          },
          "en": {
            "title": "Balancing the pole",
            "description": "An app that demonstrates the process of performing reinforcement learning using TensorFlow. The goal of the process is to balance the rod for as long as possible.",
            "howTo": "When you press the training button, a game to avoid knocking over the bar begins. The game repeats 20 games and the weight update process a total of 20 times. As the repetition continues, you have to hold the bar for increasingly longer times (steps). It won't knock you down. You can also change settings like number of repetitions, etc."
          }
        }
      },
      {
        "name": "dqnSnake",
        "href": "/modules/dqnSnake/index.html",
        "title": "스네이크 (DQN)",
        "license": "Apache License 2.0",
        "description": "DQN을 활용하여 스네이크 게임을 학습하는 과정을 볼 수 있습니다. 벽과 자신의 몸에 부딪히면 마이너스 보상을, 과일을 먹으면 플러스 보상을 받도록 강화학습이 진행되었습니다.",
        "source": "https://github.com/tensorflow/tfjs-examples/tree/master/snake-dqn",
        "howTo": "자동 실행 버튼을 누르면 게임이 시작됩니다. 스텝 버튼을 누르면 게임의 진행 과정을 한 단계씩 볼 수 있습니다. 매 순간 에이전트가 여러 선택지 중에서 계산된 Q값을 보고 가장 높은 Q값을 선택하여 이동하는 것을 확인할 수 있습니다.",
        "bookChapter": "DQN, 게임, 학습",
        "bookPage": "107",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "スネーク (DQN)",
            "description": "DQNを活用してスネークゲームを学ぶ過程を見ることができます。壁や自分の体にぶつかるとマイナス報酬を、果物を食べるとプラス報酬を受けるように強化学習が進められました。",
            "howTo": "自動実行ボタンを押すとゲームが始まります。移動することを確認できます。"
          },
          "en": {
            "title": "Snake (DQN)",
            "description": "You can see the process of learning the snake game using DQN. Reinforcement learning was carried out so that you receive a negative reward when you hit a wall or your own body, and you receive a positive reward when you eat fruit.",
            "howTo": "When you press the autoplay button, the game starts. When you press the step button, you can see the progress of the game step by step. At each moment, the agent looks at the calculated Q value among several options and selects the highest Q value. You can check that it is moving."
          }
        }
      },
      {
        "name": "jupiter2048",
        "href": "/modules/jupiter2048/index.html",
        "title": "2048 AI",
        "license": "MIT",
        "description": "MCTS 알고리즘을 이용하여 2048 게임을 학습하는 과정을 볼 수 있습니다. 한번의 움직임에 많은 시뮬레이션 수를 제공하면 높은 확률로 2048에 도달할 수 있습니다.",
        "source": "https://github.com/xtrp/jupiter",
        "howTo": "페이지를 열면 인공지능이 바로 2048 게임을 시작합니다. 사용자가 게임을 직접 조작할 수는 없지만, 화면 오른쪽 위의 이동 당 시뮬레이션 숫자를 변경하여 한번 움직일 때 몇 번을 생각하고 움직일지 설정할 수 있습니다. 숫자가 클수록 컴퓨터의 부하가 커지지만 결과가 좋을 확률이 높아집니다.",
        "bookChapter": "게임, 학습",
        "bookPage": "111",
        "webcam": false,
        "anotherName": "다른게임",
        "anotherHref": "https://aj-r.github.io/2048-AI",
        "lang": {
          "ja": {
            "title": "2048 AI",
            "description": "MCTS アルゴリズムを使用して 2048 ゲームを学習する過程を見ることができます。一度の動きに多くのシミュレーション数を提供すると、高い確率で 2048 に達することができます。",
            "howTo": "ページを開くと、人工知能がすぐに2048ゲームを開始します。ユーザーがゲームを直接操作することはできませんが、画面右上の移動ごとにシミュレーション番号を変更して、一度動くときに何回を考えて動くか設定できます。数値が大きいほどコンピュータの負荷が大きくなりますが、結果が良い可能性が高くなります。",
            "anotherName": "他のゲーム"
          },
          "en": {
            "title": "2048 AI",
            "description": "You can see the process of learning the 2048 game using the MCTS algorithm. If you provide a large number of simulations in one move, you can reach 2048 with a high probability.",
            "howTo": "When you open the page, the AI ​​will immediately start playing the 2048 game. You cannot control the game directly, but you can change the number of simulations per move in the upper right corner of the screen to determine how many times to think before making each move. You can set it: the larger the number, the greater the load on your computer, but the more likely you are to get good results.",
            "anotherName": "Another game",
            "anotherHref": "https://aj-r.github.io/2048-AI"
          }
        }
      },
      {
        "name": "gorillasAi",
        "href": "/modules/gorillas/ai/index.html",
        "title": "머신러닝 고릴라",
        "license": "MIT",
        "description": "지도학습 알고리즘을 이용하여 고릴라 게임 플레이 방법을 가르쳤습니다. TensorFlow로 제작한 간단한 신경망을 이용했습니다.",
        "source": "https://github.com/ssusnic/Machine-Learning-Gorillas",
        "howTo": "플레이 버튼을 누르면 두 고릴라가 서로를 맞추려고 바나나를 던지는 것을 볼 수 있습니다. 학습 데이터셋이 0인 경우는 서로를 잘 맞추지 못하지만, 데이터셋이 충분하면 대부분 한번에 맞출 수 있습니다. 화면 오른쪽 아래의 데이터 수집 시작과 모델 훈련 버튼을 이용하여 고릴라들을 추가 훈련시킬 수도 있습니다.",
        "bookChapter": "게임, 학습",
        "bookPage": "111",
        "webcam": false,
        "anotherName": "게임하기",
        "anotherHref": "/modules/gorillas/game/index.html",
        "lang": {
          "ja": {
            "title": "機械学習ゴリラ",
            "description": "指導学習アルゴリズムを使用してゴリラのゲームプレイ方法を教えました。 TensorFlowで作成した単純なニューラルネットワークを使用しました。",
            "howTo": "プレイボタンを押すと、2つのゴリラがお互いを合わせようとバナナを投げるのを見ることができます。以下のデータ収集の開始とモデルトレーニングボタンを使用して、ゴリラをさらにトレーニングすることもできます。",
            "anotherName": "ゲームする"
          },
          "en": {
            "title": "Machine Learning Gorilla",
            "description": "We used a supervised learning algorithm to teach Gorilla how to play the game. We used a simple neural network built with TensorFlow.",
            "howTo": "If you press the play button, you will see the two gorillas throwing bananas trying to hit each other. If the training dataset is 0, they will not be able to guess each other very well, but if the dataset is large enough, most of them will be able to guess each other in one try. Right side of the screen You can also further train the gorillas using the Start data collection and Train model buttons below.",
            "anotherName": "Playing a Game",
            "anotherHref": "/modules/gorillas/game/index.html"
          }
        }
      },
      {
        "name": "flappyAi",
        "href": "/modules/flappy/index.html",
        "title": "머신러닝 플래피 버드",
        "license": "MIT",
        "description": "신경망과 유전 알고리즘을 이용하여 플래피 버드 게임 학습 과정을 볼 수 있습니다. 새들은 세대를 거치며 이전 세대의 정보를 바탕으로 더 잘 날게 됩니다.",
        "source": "https://github.com/ssusnic/Machine-Learning-Flappy-Bird",
        "howTo": "페이지를 열면 10마리의 새들이 플래피 버드 게임을 진행합니다. 10마리의 새가 모두 탈락하면 한 세대의 게임이 끝나고, 이후 새로운 세대의 게임이 시작됩니다.",
        "bookChapter": "게임, 학습",
        "bookPage": "110",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "機械学習フラッピーバード",
            "description": "ニューラルネットワークと遺伝的アルゴリズムを使用して、フロッピーバードゲームの学習プロセスを見ることができます。",
            "howTo": "ページを開けると、10匹の鳥がフラッピーバードゲームを進行します。"
          },
          "en": {
            "title": "Machine Learning Flappy Bird",
            "description": "You can see the Flappy Bird game learning process using neural networks and genetic algorithms. As the birds pass through generations, they become better at flying based on information from previous generations.",
            "howTo": "When you open the page, 10 birds will be playing Flappy Bird. When all 10 birds are eliminated, one generation of the game will end, and a new generation will begin."
          }
        }
      },
      {
        "name": "tetrisAi",
        "href": "/modules/tetrisAi/index.html",
        "title": "테트리스 AI",
        "license": "None",
        "description": "CNN을 활용하여 테트리스 게임을 학습하는 인공지능을 만들었습니다. 챔피언의 경기 데이터와 유사하게 블록을 놓도록 반복 훈련되었습니다.",
        "source": "https://www.askforgametask.com/tutorial/machine-learning/ai-plays-tetris-with-cnn/",
        "howTo": "실행하면 인공지능이 바로 게임을 진행합니다. 아직 훈련되지 않은 상태라 결과가 좋지 않을 수 있습니다. 훈련 버튼을 누르면 처음부터 훈련시킬 수 있지만, 한 번에 5,000번씩만 훈련하고 시간이 많이 걸립니다. 로드 버튼을 누르면 75,000번 훈련된 모델이 로드되며, 이 모델은 상당히 뛰어난 게임 플레이 능력을 보여줍니다.",
        "bookChapter": "CNN, 게임, 텐서플로우, 학습",
        "bookPage": "124",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "テトリス AI",
            "description": "CNNを活用してテトリスゲームを学習する人工知能を作成しました。チャンピオンの試合データと同様に、ブロックをドロップするように繰り返し訓練されました。",
            "howTo": "実行すると人工知能がすぐにゲームを進行します。 「ロード」ボタンを押すと、75,000回トレーニングされたモデルがロードされ、このモデルはかなり優れたゲームプレイ能力を示しています。"
          },
          "en": {
            "title": "Tetris AI",
            "description": "Using CNN, we created an artificial intelligence that learns the game of Tetris. It is repeatedly trained to place blocks similar to the match data of champions.",
            "howTo": "When you run it, the AI ​​will start playing the game right away. Since it has not been trained yet, the results may not be good. You can train it from the beginning by pressing the training button, but it will only train 5,000 times at a time and the time will run out. It takes a long time. When you hit the load button, it loads a model that has been trained 75,000 times, and it shows pretty good gameplay."
          }
        }
      },
      {
        "name": "emojiScavengerHunt",
        "href": "/modules/emojiScavengerHunt/index.html",
        "title": "이모티콘 보물 찾기",
        "license": "Apache License 2.0",
        "description": "제시된 이모티콘과 같은 사물을 주변에서 찾는 게임입니다. CNN을 통해 이미지를 예측하고, 예측과 정답(이모티콘)의 일치 여부를 확인합니다.",
        "source": "https://github.com/google/emoji-scavenger-hunt",
        "howTo": "매 스테이지마다 사물 이모티콘이 랜덤하게 제시됩니다. 이 이모티콘과 같은 사물을 찾아서 카메라에 비추면 다음 스테이지로 넘어갈 수 있습니다. 정답 판정은 예측 상위 결과 2개 중 하나가 이모티콘과 일치하는지 여부로 결정됩니다. 같은 사물이라도 학습에 사용된 사물과 다른 형태라서 오답으로 판정할 수 있습니다.",
        "bookChapter": "인식, 재미, CNN",
        "bookPage": "35, 75",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "絵文字宝探し",
            "description": "提示された絵文字のようなものを周辺で探すゲームです。CNNを介して画像を予測し、予測と正解（絵文字）の一致を確認します。",
            "howTo": "ステージごとにモノの絵文字がランダムに表示されます。この絵文字のようなものを見つけてカメラに照らすと、次のステージに進むことができます。同じようなものでも学習に使用されたものとは異なる形なので誤解で判定できます。"
          },
          "en": {
            "title": "Emoji Treasure Hunt",
            "description": "This is a game where you find objects around you that match the presented emoticon. Images are predicted through CNN, and the prediction matches the correct answer (emoticon).",
            "howTo": "In each stage, an object emoticon is presented randomly. Find an object like this emoticon and point it at the camera to proceed to the next stage. The correct answer is determined by whether one of the two predicted top results matches the emoticon. Even if the object is the same, it may be judged as an incorrect answer because it is in a different form from the object used for learning."
          }
        }
      },
      {
        "name": "teachablemachine",
        "href": "https://teachablemachine.withgoogle.com",
        "title": "티처블 머신",
        "license": "External Site",
        "description": "누구나 머신러닝 모델을 쉽고 빠르게 만들 수 있도록 제작된 웹 기반 머신러닝 학습 도구입니다. 이미지, 오디오, 포즈 모델을 제작할 수 있습니다.",
        "source": "https://teachablemachine.withgoogle.com",
        "howTo": "이미지, 오디오, 포즈 프로젝트 중 하나 선택합니다. 분류를 원하는 클래스의 개수와 이름을 정하고, 각 클래스에 웹캠, 사진, 음성 등의 데이터를 추가합니다. 데이터는 클래스별로 일관성이 있어야 하며, 양이 많을수록 학습 결과가 좋아집니다. 학습을 진행하면 결과를 확인할 수 있고, 외부에 공유해서 사용할 수도 있습니다.",
        "bookChapter": "실습",
        "bookPage": "78",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "ティーチャーブルマシン",
            "description": "誰もが機械学習モデルを簡単かつ迅速に作成できるように設計されたウェブベースの機械学習学習ツールです。画像、オーディオ、ポーズモデルを作成できます。",
            "howTo": "画像、オーディオ、ポーズプロジェクトのいずれかを選択します。分類したいクラスの数と名前を付け、各クラスにウェブカメラ、写真、音声などのデータを追加します。データはクラスごとに一貫性がなければなりません。 、量が多いほど学習結果が良くなります。学習を進めると結果を確認でき、外部に共有して使用することもできます。"
          },
          "en": {
            "title": "Teachable Machine",
            "description": "It is a web-based machine learning learning tool designed to allow anyone to quickly and easily create machine learning models. You can create image, audio, and pose models.",
            "howTo": "Choose one of the Image, Audio, or Pose projects. Specify the number and name of the classes you want to classify, and add data such as webcam, photo, voice, etc. to each class. The data must be consistent for each class. , the larger the amount, the better the learning results. As you proceed with learning, you can check the results, and you can also share them and use them externally."
          }
        }
      },
      {
        "name": "performanceRnn",
        "href": "/modules/performanceRnn/index.html",
        "title": "피아노 작곡 RNN",
        "license": "Apache License 2.0",
        "description": "Performance RNN 모델을 활용하여 조표의 사용 빈도를 참고해서 곡을 창작해줍니다. 모델은 LSTM을 이용하여 음악적 구조와 패턴을 학습했습니다.",
        "source": "https://github.com/magenta/magenta-demos/tree/main/performance_rnn",
        "howTo": "페이지 로드 후 화면을 클릭하면 피아노 곡이 연주됩니다. 화면 왼쪽 조절 영역에서 켜기를 체크하면 조표들의 숫자를 바꿀 수 있습니다. 숫자가 클수록 그 조표를 더 많이 참고해서 작곡해줍니다. 음표 밀도를 조절해서 동시에 연주하는 음의 수를 바꿀 수 있고, 입력 볼륨을 조절해서 음의 강도를 바꿀 수 있습니다.",
        "bookChapter": "음악, RNN",
        "bookPage": "132",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "ピアノ作曲 RNN",
            "description": "Performance RNN モデルを活用して、表の使用頻度を参考に曲を作成します。モデルは LSTM を使用して音楽構造とパターンを学習しました。",
            "howTo": "ページを読み込んだ後、画面をクリックするとピアノの曲が演奏されます。を調整して同時に演奏する音の数を変えることができ、入力音量を調節して音の強度を変えることができます。"
          },
          "en": {
            "title": "RNN for piano composition",
            "description": "Using the Performance RNN model, a song is created by referring to the frequency of use of key signatures. The model learned musical structures and patterns using LSTM.",
            "howTo": "After loading the page, click on the screen to play the piano song. You can change the number of key signatures by checking On in the control area on the left side of the screen. The larger the number, the more the composition is composed with reference to that key signature. Note density You can change the number of notes played simultaneously by adjusting , and you can change the intensity of the notes by adjusting the input volume."
          }
        }
      },
      {
        "name": "latentCycles",
        "href": "/modules/latentCycles/index.html",
        "title": "멜로디 루프 만들기",
        "license": "None",
        "description": "MusicVAE 모델을 활용하여 반복되는 멜로디를 생성하는 앱입니다. MusicVAE는 여러 멜로디를 부드럽게 연결하여 조화로운 멜로디를 만들 수 있습니다.",
        "source": "https://codepen.io/teropa/details/rdoPbG",
        "howTo": "화면 왼쪽과 오른쪽에 있는 조표와 코드를 선택하고, 화면 중앙에서 리듬을 선택하면 모델이 자동으로 조화로운 멜로디를 생성해줍니다. 리듬은 여러 개를 선택하거나 해제할 수 있습니다.",
        "bookChapter": "음악, RNN",
        "bookPage": "138",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "メロディーループの作成",
            "description": "MusicVAE モデルを活用して繰り返しのメロディを作成するアプリです",
            "howTo": "画面の左右にある調印とコードを選択し、画面の中央でリズムを選択すると、モデルは自動的に調和のとれたメロディを生成します。リズムは複数を選択または解除できます。"
          },
          "en": {
            "title": "Creating a melody loop",
            "description": "This is an app that utilizes the MusicVAE model to generate repeating melodies. MusicVAE can create harmonious melodies by smoothly connecting multiple melodies.",
            "howTo": "Select a key signature and chord on the left and right sides of the screen, select a rhythm in the center of the screen, and the model will automatically generate a harmonious melody. You can select or deselect multiple rhythms."
          }
        }
      },
      {
        "name": "neuralArpeggiator",
        "href": "/modules/neuralArpeggiator/index.html",
        "title": "아르페지오 패턴 작곡",
        "license": "None",
        "description": "Magenta와 Improv RNN를 활용하여 아르페지오 패턴을 연주하게 제작하였습니다. Improv RNN은 기본 코드 진행에 따라 멜로디를 조건부로 생성합니다.",
        "source": "https://codepen.io/teropa/details/ddqEwj",
        "howTo": "화면의 건반 중 하나를 계속 누르고 있으면 그 음을 중심으로 아르페지오 패턴이 연주됩니다. 화면 위쪽에서 곡의 온도와 패턴 길이 등을 조절할 수 있습니다.",
        "bookChapter": "음악, RNN",
        "bookPage": "138",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "アルペジオパターン作曲",
            "description": "Magenta と Improv RNN を活用してアルペジオパターンを演奏します。",
            "howTo": "画面上の鍵盤の1つを押し続けると、その音を中心にアルペジオパターンが演奏されます。画面上部の曲の温度やパターンの長さなどを調整できます。"
          },
          "en": {
            "title": "Arpeggio pattern composition",
            "description": "We created an arpeggio pattern to play using Magenta and Improv RNN. Improv RNN conditionally generates a melody based on the basic chord progression.",
            "howTo": "If you hold down one of the keys on the screen, an arpeggio pattern will play around that note. You can adjust the song's temperature, pattern length, etc. at the top of the screen."
          }
        }
      },
      {
        "name": "neuralDrumMachine",
        "href": "/modules/neuralDrumMachine/index.html",
        "title": "신경망 드럼 머신",
        "license": "None",
        "description": "사전 훈련된 드럼 RNN 모델을 이용하여 만든 드럼 작곡 앱입니다. 씨앗 패턴을 제공하면 이를 바탕으로 다음 패턴을 연속적으로 생성해줍니다.",
        "source": "https://codepen.io/teropa/details/JLjXGK",
        "howTo": "화면에 있는 회색 선 왼쪽에 있는 빈 사각형들을 클릭하면 빨간색으로 표시됩니다. 적당한 사각형들을 클릭하고 회색 선 위에 있는 플레이 버튼을 누르면 잠시 후 오른쪽에 트랙이 자동으로 생성되면서 곡이 재생됩니다. 화면 아래에서 패턴 길이, 템포, 스윙, 온도를 조정할 수 있습니다.",
        "bookChapter": "음악, RNN",
        "bookPage": "38, 131",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "ニューラルネットワークドラムマシン",
            "description": "事前に訓練されたドラム RNN モデルを使用して作成されたドラム作曲アプリです",
            "howTo": "画面上の灰色の線の左側にある空白の四角形をクリックすると赤色で表示されます。適切な四角形をクリックして灰色の線の上にある再生ボタンを押すと、しばらくすると右側にトラックが自動的に作成され、曲が再生されます。画面の下でパターンの長さ、テンポ、スイング、温度を調整できます。"
          },
          "en": {
            "title": "Neural Network Drum Machine",
            "description": "This is a drum composition app created using a pre-trained drum RNN model. If you provide a seed pattern, it continuously generates the next pattern based on it.",
            "howTo": "If you click on the empty squares to the left of the gray line on the screen, they will turn red. Click on the appropriate squares and press the play button above the gray line. After a while, a track will be automatically created on the right and the song will play. .You can adjust pattern length, tempo, swing, and temperature below the screen."
          }
        }
      },
      {
        "name": "mkTfjs",
        "href": "/modules/mkTfjs/index.html",
        "title": "동작 인식 격투 게임",
        "license": "MIT",
        "description": "TensorFlow와 카메라를 이용한 동작 인식으로 캐릭터를 조종할 수 있는 게임입니다. 게임 캐릭터가 사용자의 행동을 따라서 상대방을 공격합니다.",
        "source": "https://github.com/mgechev/mk-tfjs",
        "howTo": "카메라가 전신을 비추도록 멀리 떨어진 상태에서 화면의 왼쪽이나 오른쪽으로 이동합니다. 손으로 펀치를 하거나 발로 발차기를 하면 캐릭터가 동작을 따라 합니다. 게임을 다시 시작하려면 웹페이지를 새로고침 하면 됩니다.",
        "bookChapter": "인식, 재미, 게임, CNN, RNN",
        "bookPage": "139",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "アクション認識格闘ゲーム",
            "description": "TensorFlowとカメラを使った動き認識でキャラクターを操縦できるゲームです。ゲームキャラクターがユーザーの行動に沿って相手を攻撃します。",
            "howTo": "カメラが全身を照らすように遠く離れた状態で画面の左右に移動します。できます。"
          },
          "en": {
            "title": "Motion recognition fighting game",
            "description": "This is a game where you can control your character through motion recognition using TensorFlow and a camera. The game character follows the user's actions and attacks the opponent.",
            "howTo": "Move to the left or right of the screen so the camera covers your entire body. Punch with your hand or kick with your foot and your character will follow your movements. Refresh the webpage to restart the game. Just do it."
          }
        }
      },
      {
        "name": "webcamTransferLearning",
        "href": "/modules/webcamTransferLearning/index.html",
        "title": "팩맨 머신러닝",
        "license": "Apache License 2.0",
        "description": "이미지 인식을 통해 방향을 조작할 수 있도록 만든 팩맨 게임입니다. 사전 훈련된 모바일넷 모델을 4개 방향의 동작 인식에 활용하였습니다.",
        "source": "https://github.com/tensorflow/tfjs-examples/tree/master/webcam-transfer-learning",
        "howTo": "캐릭터를 상하좌우 4개 방향으로 조작하기 위해서는 각 방향별로 학습을 위한 이미지 데이터가 필요합니다. 각 방향을 표시할 수 있는 모션을 샘플 추가 버튼을 눌러 촬영하고, 모델 훈련 버튼을 눌러 학습시킵니다. 이후 시작 버튼을 누르고 각 방향을 나타내는 모션을 취하면 인식된 방향대로 캐릭터가 움직입니다.",
        "bookChapter": "인식, 학습, 재미",
        "bookPage": "94",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "パックマン機械学習",
            "description": "画像認識を通じて方向を操作できるようにしたパックマンゲームです。 事前訓練されたモバイルネットモデルを4方向の動き認識に活用しました。",
            "howTo": "キャラクターを上下左右4つの方向に操作するには、各方向ごとに学習のための画像データが必要です。 各方向を表示できるモーションをサンプル追加ボタンを押して撮影し、モデルトレーニングボタンを押して学習後、スタートボタンを押して各方向を表すモーションをとると、認識された方向にキャラクターが移動します。"
          },
          "en": {
            "title": "Pac-Man Machine Learning",
            "description": "This is a Pac-Man game that allows you to manipulate direction through image recognition. A pre-trained MobileNet model was used to recognize motion in four directions.",
            "howTo": "In order to manipulate the character in the four directions, up, down, left, right, and left, image data for learning is required for each direction. Click the Add Sample button to film motions that can display each direction, and then click the Model Training button. After learning, press the start button and make motions representing each direction, and the character will move in the recognized direction."
          }
        }
      },
      {
        "name": "kerasJs",
        "href": "/modules/kerasJs/index.html",
        "title": "Keras.js",
        "license": "MIT",
        "description": "Keras는 인공지능을 쉽고 빠르게 구현하도록 돕는 딥러닝 라이브러리입니다. 데모에서는 브라우저에서 Keras의 학습 과정과 성능을 확인할 수 있습니다.",
        "source": "https://github.com/transcranial/keras-js",
        "howTo": "데모는 필기 숫자 인식, 오토 인코더, GAN, 이미지 인식, 감정분류 LSTM, 해상도 높이기로 구성되어 있습니다. 원하는 데모를 선택해서 사용합니다. 화면 아래쪽에서는 각 기능이 어떤 과정을 거치며 진행되는지 확인할 수 있습니다.",
        "bookChapter": "실습, CNN",
        "bookPage": "115",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "Keras.js",
            "description": "Kerasは、人工知能を簡単かつ迅速に実装するのに役立つディープラーニングライブラリです。デモでは、ブラウザでKerasの学習プロセスとパフォーマンスを確認できます。",
            "howTo": "デモは、手書きの数字認識、オートエンコーダ、GAN、画像認識、感情分類LSTM、解像度の高さで構成されています。希望のデモを選択して使用します。確認できます。"
          },
          "en": {
            "title": "Keras.js",
            "description": "Keras is a deep learning library that helps you quickly and easily implement artificial intelligence. In the demo, you can check out Keras' learning process and performance in your browser.",
            "howTo": "The demo consists of handwritten digit recognition, auto encoder, GAN, image recognition, emotion classification LSTM, and resolution increase. Select the demo you want and use it. At the bottom of the screen, you can see what process each function goes through. “I can confirm."
          }
        }
      },
      {
        "name": "convnetJs",
        "href": "/modules/convnetJs/index.html",
        "title": "ConvNetJS",
        "license": "MIT",
        "description": "ConvNetJS는 브라우저에서 딥러닝 모델을 학습할 수 있는 라이브러리입니다. 데모를 통해 신경망의 학습 과정과 결과를 시각화해서 볼 수 있습니다.",
        "source": "https://github.com/karpathy/convnetjs/tree/master/demo",
        "howTo": "데모는 필기 숫자 인식, 이미지 인식, 분류, 회귀, 오토 인코더, DQN으로 구성되어 있습니다. 데모 중 하나를 클릭하면, 각 데모의 학습 과정을 실시간으로 확인할 수 있습니다. 설정을 변경하면 설정 값에 따른 결과의 변화도 알 수 있습니다.",
        "bookChapter": "실습, CNN",
        "bookPage": "120",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "ConvNetJS",
            "description": "ConvNetJSは、ブラウザでディープラーニングモデルを学習できるライブラリです。デモを使用すると、ニューラルネットワークの学習プロセスと結果を視覚化することができます。",
            "howTo": "デモは手書き数字認識、画像認識、分類、回帰、オートエンコーダ、DQNで構成されています。デモのいずれかをクリックすると、各デモの学習過程をリアルタイムで確認できます。設定値による結果の変化もわかります。"
          },
          "en": {
            "title": "ConvNetJS",
            "description": "ConvNetJS is a library that allows you to train deep learning models in the browser. Through the demo, you can visualize the learning process and results of the neural network.",
            "howTo": "The demos consist of handwritten digit recognition, image recognition, classification, regression, autoencoder, and DQN. By clicking on one of the demos, you can see the training process for each demo in real time. Change the settings. You can also see changes in results depending on the settings."
          }
        }
      },
      {
        "name": "rpsTfjs",
        "href": "/modules/rpsTfjs/index.html",
        "title": "가위바위보 머신러닝",
        "license": "MIT",
        "description": "TensorFlow를 이용한 가위바위보 이미지 인식 학습 과정을 단계별로 살펴볼 수 있습니다.",
        "source": "https://github.com/GantMan/rps_tfjs_demo",
        "howTo": "가위바위보 이미지 인식 학습 과정을 확인하기 위해서 페이지에 있는 파란색 버튼들을 위에서부터 순서대로 누르면 됩니다. 데이터 준비부터 모델 생성, 학습, 학습 결과 확인 과정을 오른쪽에 표시되는 결과 화면을 통해 볼 수 있습니다. 웹캠을 실행해서 직접 학습 결과를 테스트하는 것도 가능합니다.",
        "bookChapter": "실습, CNN, 텐서플로우",
        "bookPage": "",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "ハサミロックマシンラーニング",
            "description": "TensorFlowを使用したはさみロック画像認識学習プロセスを段階的に見ることができます。",
            "howTo": "はさみロック画像認識学習過程を確認するために、ページの青いボタンを上から順に押すだけです。また、ウェブカメラを起動して直接学習結果をテストすることもできます。"
          },
          "en": {
            "title": "Rock-Paper-Scissors Machine Learning",
            "description": "You can take a step-by-step look at the rock-paper-scissors image recognition learning process using TensorFlow.",
            "howTo": "To check the rock-paper-scissors image recognition learning process, just press the blue buttons on the page in order from the top. The process from data preparation to model creation, learning, and learning results confirmation is shown on the results screen on the right. You can view it. You can also launch a webcam and test the learning results yourself."
          }
        }
      },
      {
        "name": "tensorspace",
        "href": "https://tensorspace.org/html/playground/index.html",
        "title": "텐서플로우 시각화",
        "license": "Apache License 2.0",
        "description": "TensorFlow로 사전 훈련된 딥러닝 모델을 로드해서 이를 3D 시각화 장면으로 출력합니다. 각 모델의 처리 과정을 시각화하여 볼 수 있습니다.",
        "source": "https://github.com/tensorspace-team/tensorspace",
        "howTo": "화면 왼쪽에 있는 모델 중 하나를 선택합니다. 모델이 로드되면 오른쪽의 입력 영역에 필요한 값을 넣고, 화면 중앙에서 마우스로 드래그, 확대/축소해서 처리 과정을 확인합니다. 예를 들어, Lenet 모델의 경우 오른쪽 입력 영역에 숫자를 그리면 화면 중앙에서 숫자 인식 과정을 확인할 수 있습니다.",
        "bookChapter": "실습, 텐서플로우",
        "bookPage": "126",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "テンソルフローの可視化",
            "description": "TensorFlowで事前トレーニングされたディープラーニングモデルをロードして、3Dビジュアライゼーションシーンに出力します。各モデルの処理プロセスを可視化して表示できます。",
            "howTo": "画面の左側にあるモデルの1つを選択します。モデルがロードされたら、右側の入力領域に必要な値を配置し、画面の中央からマウスでドラッグ、ズームして処理を確認します。 、Lenetモデルの場合、右側の入力領域に数字を描くと、画面の中央で数字認識プロセスを確認できます。"
          },
          "en": {
            "title": "TensorFlow Visualization",
            "description": "Load deep learning models pre-trained with TensorFlow and output them as 3D visualization scenes. You can visualize the processing of each model.",
            "howTo": "Select one of the models on the left side of the screen. Once the model is loaded, enter the required values ​​in the input area on the right and check the progress by dragging and zooming with the mouse in the center of the screen. For example: , In the case of the Lenet model, if you draw a number in the right input area, you can check the number recognition process in the center of the screen."
          }
        }
      },
      {
        "name": "tensorflowRexRun",
        "href": "/modules/tensorflowRexRun/index.html",
        "title": "텐서플로우 티라노 달리기",
        "license": "None",
        "description": "TensorFlow를 기반으로 티라노 캐릭터가 여러 유형의 훈련을 통해 장애물을 피하는 방법을 학습하는 프로그램입니다.",
        "source": "https://github.com/MagicCube/tensorflow-rex-run",
        "howTo": "페이지를 열면 랜덤에서부터 유전 + 신경망까지 훈련 유형 목록이 표시됩니다. 확인을 원하는 유형을 클릭하면 티라노가 장애물에 부딪칠 때까지 한 세대가 진행됩니다. 세대를 반복하며 더 오래 살아남게 되는데, 각 학습 유형별로 학습 속도의 차이를 비교할 수 있습니다.",
        "bookChapter": "실습, 학습, 텐서플로우",
        "bookPage": "",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "テンソルフローティラノランニング",
            "description": "TensorFlowに基づいて、ティラノのキャラクターがさまざまな種類のトレーニングで障害物を回避する方法を学習するプログラムです。",
            "howTo": "ページを開くと、ランダムから遺伝+ニューラルネットワークまでのトレーニングタイプのリストが表示されます。各学習タイプで学習速度の違いを比較できます。"
          },
          "en": {
            "title": "TensorFlow Tyrano Running",
            "description": "A program based on TensorFlow where the Tyrannosaurus character learns how to avoid obstacles through several types of training.",
            "howTo": "When you open the page, you will see a list of training types, from Random to Genetic + Neural Networks. Click on the type you want to check and your Tyranno will advance through one generation until it hits an obstacle. Repeat the generations to survive longer. “You can compare the difference in learning speed for each learning type."
          }
        }
      },
      {
        "name": "cnnExplainer",
        "href": "/modules/cnnExplainer/index.html",
        "title": "CNN 시각적 설명",
        "license": "MIT",
        "description": "사용자가 CNN의 내부 작동 방식을 쉽게 이해할 수 있도록 구현한 프로그램입니다. 이미지 인식 과정을 단계별로 시각화해서 볼 수 있습니다.",
        "source": "https://github.com/poloclub/cnn-explainer",
        "howTo": "화면 왼쪽 위에 있는 이미지들 중 하나를 선택하면 해당 이미지의 인식 과정을 확인할 수 있습니다. conv나 relu, max_pool 층에 위치한 이미지를 클릭하면 앞 단계와 현재 요소가 어떻게 연결되는지 상세하게 볼 수 있습니다.",
        "bookChapter": "실습, CNN",
        "bookPage": "126",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "CNN ビジュアル説明",
            "description": "ユーザーが CNN の内部動作を理解しやすくするために実装したプログラムです。画像認識プロセスを段階的に視覚化して表示できます。",
            "howTo": "画面の左上にある画像の1つを選択すると、その画像の認識プロセスを確認できます。できます。"
          },
          "en": {
            "title": "CNN Visual Description",
            "description": "This is a program implemented to help users easily understand the inner workings of CNN. You can visualize the image recognition process step by step.",
            "howTo": "You can check the recognition process of that image by selecting one of the images in the upper left corner of the screen. If you click on an image located in the conv, relu, or max_pool layer, you can see in detail how the previous step and the current element are connected. can."
          }
        }
      },
      {
        "name": "ganLab",
        "href": "/modules/ganLab/index.html",
        "title": "GAN 시각적 설명",
        "license": "Apache License 2.0",
        "description": "GAN의 학습 과정을 대화형 시각화 도구로 실시간으로 살펴볼 수 있는 프로그램입니다. 2D 데이터에 대한 생성자와 판별자의 작동 과정을 예시로 제시하였습니다.",
        "source": "https://github.com/poloclub/ganlab",
        "howTo": "화면 위쪽 데이터 분포에서 원하는 데이터 분포를 선택합니다. 그리고 시작 버튼을 클릭하면 화면 오른쪽에서 초록색 점들(실제 샘플) 위로 보라색 점들(가짜 샘플)이 겹쳐지려고 합니다. 배경의 색도 계속 변하게 되는데 흰색에 가까운 회색은 판별자가 더 이상 가짜 샘플과 실제 샘플을 구별할 수 없다는 의미입니다.",
        "bookChapter": "실습, GAN",
        "bookPage": "144",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "GAN ビジュアル説明",
            "description": "GANの学習プロセスをインタラクティブなビジュアライゼーションツールでリアルタイムで見ることができるプログラムです",
            "howTo": "画面上部のデータ分布から希望のデータ分布を選択します。そして、スタートボタンをクリックすると、画面の右側で緑色の点（実際のサンプル）の上に紫色の点（偽のサンプル）が重なっていきます。背景の色も変化し続けます。白に近い灰色は、判別者が偽のサンプルと実際のサンプルを区別できないことを意味します。"
          },
          "en": {
            "title": "GAN Visual Explanation",
            "description": "This is a program that allows you to examine the learning process of GAN in real time with an interactive visualization tool. The operation process of the generator and discriminator for 2D data is presented as an example.",
            "howTo": "Select the desired data distribution from the data distribution at the top of the screen. Then, when you click the start button, purple dots (fake samples) will overlap on the green dots (real samples) on the right side of the screen. The background color will also change continuously. Gray, close to white, means the discriminator can no longer distinguish between fake and real samples."
          }
        }
      },
      {
        "name": "huggingFaceGan",
        "href": "https://huggingface.co/CodingTeading",
        "title": "HuggingFace GAN 예제",
        "license": "External Site",
        "description": "HuggingFace는 인공지능 데이터와 모델 제작을 지원하는 서비스입니다. 스페이스 기능을 이용해서 여러 GAN 모델을 테스트 해볼 수 있습니다.",
        "source": "https://huggingface.co/CodingTeading",
        "howTo": "페이지를 열면 스페이스 영역(Spaces)에 사용 가능한 예제들이 보입니다. 이 중에서 하나를 선택해서 GAN 예제를 테스트해 보세요. 예제가 멈춰 있는 상태라면 Restart 버튼을 눌러서 다시 실행해 주세요. 사람이나 동물 이미지를 생성하거나, 그림체를 변화시키고 해상도를 높일 수 있는 예제가 있습니다.",
        "bookChapter": "GAN, 그림",
        "bookPage": "153",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "HuggingFace GAN の例",
            "description": "HuggingFaceは、人工知能データとモデル作成をサポートするサービスです。スペース機能を使用して複数のGANモデルをテストできます。",
            "howTo": "ページを開くと、スペース領域（Spaces）に利用可能な例が表示されます。これらの中から1つを選択してGANの例をテストしてみてください。動物の画像を作成したり、画像を変更したり解像度を上げたりする例があります。"
          },
          "en": {
            "title": "HuggingFace GAN Example",
            "description": "HuggingFace is a service that supports artificial intelligence data and model creation. You can test several GAN ​​models using the space function.",
            "howTo": "When you open the page, you will see examples available in the Spaces. Select one of them to test the GAN example. If the example is frozen, click the Restart button to run it again. There are examples of creating animal images, changing the font and increasing the resolution."
          }
        }
      },
      {
        "name": "animeGan",
        "href": "/modules/animeGan/index.html",
        "title": "GAN 애니메이션",
        "license": "None",
        "description": "AnimeGAN 모델을 이용해서 풍경 사진을 애니메이션화 할 수 있는 서비스입니다.",
        "source": "https://github.com/TonyLianLong/AnimeGAN.js",
        "howTo": "먼저 풍경 이미지 파일을 준비해야 합니다. 인터넷 등에서 받은 풍경 이미지 파일을 선택하고, 이미지 크기를 선택한 후 만들기를 누르면 애니메이션화된 이미지가 생성됩니다.",
        "bookChapter": "GAN, 그림",
        "bookPage": "151",
        "webcam": false,
        "anotherName": "버전3 체험",
        "anotherHref": "https://huggingface.co/spaces/TachibanaYoshino/AnimeGANv3",
        "lang": {
          "ja": {
            "title": "GAN アニメ",
            "description": "AnimeGANモデルを利用して風景写真をアニメーション化できるサービスです。",
            "howTo": "最初に風景画像ファイルを準備する必要があります。インターネットなどで受け取った風景画像ファイルを選択し、画像サイズを選択して[作成]を押すとアニメーション化された画像が作成されます。",
            "anotherName": "バージョン3体験"
          },
          "en": {
            "title": "GAN Animation",
            "description": "This is a service that allows you to animate landscape photos using the AnimeGAN model.",
            "howTo": "You must first prepare a landscape image file. Select a landscape image file received from the Internet, etc., select the image size, and press Create to create an animated image.",
            "anotherName": "Try Version 3",
            "anotherHref": "https://huggingface.co/spaces/TachibanaYoshino/AnimeGANv3"
          }
        }
      },
      {
        "name": "aiDuet",
        "href": "https://experiments.withgoogle.com/ai/ai-duet/view/",
        "title": "RNN 듀엣 연주",
        "license": "External Site",
        "description": "다양한 MIDI 예제로 학습해서 사용자의 연주에 맞춰 다음 부분을 연주해 주는 앱입니다. 몇 개의 음을 연주하면 그에 맞춰 다음 부분이 재생됩니다.",
        "source": "https://github.com/googlecreativelab/aiexperiments-ai-duet",
        "howTo": "피아노 건반 몇 개를 누르고 잠시 기다리면 인공지능이 뒷 부분을 연주해 줍니다. 사용한 건반의 종류와 누르는 속도, 곡의 길이 등을 참고해서 연주하고, 같은 곡 구성이라도 매번 다른 연주가 나올 수 있습니다.",
        "bookChapter": "RNN, 텐서플로우",
        "bookPage": "",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "RNN デュエット演奏",
            "description": "さまざまな MIDI の例で学習し、ユーザーの演奏に合わせて次の部分を演奏してくれるアプリです",
            "howTo": "ピアノの鍵盤をいくつか押して、しばらく待つと人工知能が後部を演奏してくれます。 使用した鍵盤の種類と押す速度、曲の長さなどを参考に演奏し、同じ曲構成でも毎回異なる演奏が出ることができます。あります。"
          },
          "en": {
            "title": "RNN duet performance",
            "description": "This app learns from various MIDI examples and plays the next part according to the user's performance. When you play a few notes, the next part is played accordingly.",
            "howTo": "If you press a few piano keys and wait for a while, artificial intelligence will play the latter part. It plays by referring to the type of keys used, the speed at which you press them, and the length of the song. Even if the composition of the same song is composed, a different performance can be produced each time. there is."
          }
        }
      },
      {
        "name": "postHandwriting",
        "href": "/modules/postHandwriting/index.html",
        "title": "RNN 손 글씨",
        "license": "Creative Commons Attribution 4.0",
        "description": "LSTM을 활용해서 사용자가 작성한 글자들의 획(stroke)을 기억하고, 이를 바탕으로 예측된 글자들을 보여줍니다.",
        "source": "https://github.com/distillpub/post--handwriting",
        "howTo": "페이지가 열리면 이상한 선들이 깜빡이는 공간에 영어로 글자들을 입력해보세요. 입력한 글자 다음에 영어 글자들이 랜덤하게 생기는 것을 볼 수 있습니다. 많은 글자들을 적다 보면 점점 내가 쓴 글씨체와 유사한 글씨들을 보여주고, 때로는 내가 쓰고 있는 영어 단어에 사용될 글자와 비슷한 글자를 제시하기도 합니다.",
        "bookChapter": "RNN, 실습",
        "bookPage": "134",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "RNN 手書き",
            "description": "LSTMを活用して、ユーザーが作成した文字のストロークを記憶し、それに基づいて予測された文字を表示します。",
            "howTo": "ページが開いたら、奇妙な線がちらつく空間に英語で文字を入力してみてください。聞いて、時には私が書いている英語の単語に使われる文字に似た文字を提示することもあります。"
          },
          "en": {
            "title": "RNN handwriting",
            "description": "Using LSTM, it remembers the strokes of letters written by the user and displays predicted letters based on them.",
            "howTo": "When the page opens, try entering letters in English in the space where strange blinking lines appear. You will see English letters appearing randomly after the letters you entered. As you write down more letters, the font will gradually resemble the one you wrote. “It shows letters that are similar to the letters that will be used in the English word I am writing."
          }
        }
      },
      {
        "name": "holobooth",
        "href": "/modules/holobooth/index.html",
        "title": "Holobooth 캐릭터 애니메이션",
        "license": "MIT",
        "description": "MediaPipe의 FaceMesh를 활용해서 얼굴을 인식하고, 이를 바탕으로 가상의 아바타를 만들어 주는 앱입니다.",
        "source": "https://github.com/flutter/holobooth",
        "howTo": "시작하기를 누르고 웹캠이 얼굴을 향하게 해주세요. 아바타가 얼굴의 움직임을 따라 움직입니다. 아바타와 장면, 소품을 선택할 수 있습니다.",
        "bookChapter": "텐서플로우, 인식, 재미",
        "bookPage": "65",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "Holobooth キャラクターアニメーション",
            "description": "MediaPipeのFaceMeshを活用して顔を認識し、それに基づいて仮想アバターを作成するアプリです。",
            "howTo": "スタート」をタップしてウェブカメラに顔を向けてください。アバターは顔の動きに沿って動きます。"
          },
          "en": {
            "title": "Holobooth Character Animation",
            "description": "This is an app that uses MediaPipe's FaceMesh to recognize faces and create virtual avatars based on them.",
            "howTo": "Press Get Started and point the webcam at your face. The avatar will follow your facial movements. You can choose your avatar, scene, and props."
          }
        }
      },
      {
        "name": "makeGirlsMoe",
        "href": "/modules/makeGirlsMoe/index.html",
        "title": "만화 캐릭터 만들기",
        "license": "GPL 3.0",
        "description": "선택한 속성 값으로 얼굴 이미지를 생성하는 GAN 모델입니다. 모델의 종류와 속성 값을 변경해서 원하는 캐릭터 이미지를 만들 수 있습니다.",
        "source": "https://github.com/makegirlsmoe/makegirlsmoe_web",
        "howTo": "생성 버튼을 누르면 캐릭터가 생성됩니다. 버튼을 누를 때마다 다른 캐릭터가 생성됩니다. 모델을 변경하면 그림체를 바꿀 수 있고, 속성 값을 변경하면 캐릭터의 세부 사항을 조정할 수 있습니다.",
        "bookChapter": "GAN, 실습, 그림",
        "bookPage": "40, 146",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "漫画のキャラクターを作る",
            "description": "選択した属性値で顔画像を生成する GAN モデルです。モデルの種類と属性値を変更して、必要な文字画像を作成できます。",
            "howTo": "生成ボタンを押すとキャラクターが生成されます。ボタンを押すたびに別のキャラクターが生成されます。モデルを変更するとピクチャを変更できます。"
          },
          "en": {
            "title": "Creating a cartoon character",
            "description": "This is a GAN model that creates a face image with selected attribute values. You can create the desired character image by changing the model type and attribute values.",
            "howTo": "Press the Create button to create a character. Each time you press the button, a different character will be created. By changing the model, you can change the drawing style, and by changing the attribute values, you can adjust the details of the character."
          }
        }
      },
      {
        "name": "gestureControlled2048",
        "href": "/modules/gestureControlled2048/index.html",
        "title": "제스처로 컨트롤하는 2048",
        "license": "MIT",
        "description": "CNN을 활용한 이미지 인식기능으로 2048 게임을 진행할 수 있습니다.",
        "source": "https://github.com/jithurjacob/tensorflowjs-gesture-controlled-2048",
        "howTo": "위, 아래, 왼쪽, 오른쪽, 행동 없음에 대한 샘플을 웹캠을 이용해서 추가해주세요. 이후 훈련 버튼을 눌러 훈련시키고, 플레이 시작 버튼으로 게임을 시작하세요. 웹캠 앞에서 샘플과 유사한 이미지를 보여주면 2048을 조작할 수 있습니다.",
        "bookChapter": "텐서플로우, CNN, 실습, 게임, 재미",
        "bookPage": "94",
        "webcam": true,
        "lang": {
          "ja": {
            "title": "ジェスチャーでコントロールする 2048",
            "description": "CNNを活用した画像認識機能で2048ゲームを進めることができます。",
            "howTo": "上、下、左、右、行動なしのサンプルをウェブカメラで追加してください。」表示すると、2048を操作できます。"
          },
          "en": {
            "title": "2048 controlled with gestures",
            "description": "You can play the 2048 game with image recognition using CNN.",
            "howTo": "Add samples for up, down, left, right, and no action using the webcam. Then press the train button to train, and start the game with the start play button. In front of the webcam, add an image similar to the sample. “If you show me, I can manipulate 2048."
          }
        }
      },
      {
        "name": "pix2pixTensorflow",
        "href": "/modules/pix2pixTensorflow/index.html",
        "title": "스케치를 사진으로",
        "license": "MIT",
        "description": "Pix2Pix GAN 모델을 이용해서 스케치 등의 소스 이미지를 입력 받아 다른 형태의 이미지로 변환해주는 서비스입니다.",
        "source": "https://github.com/affinelayer/pix2pix-tensorflow",
        "howTo": "edges2cats, facades 등의 영역에서 소스 이미지 예시와 생성 결과를 확인할 수 있습니다. 지우기 버튼을 눌러 기존 스케치를 지우고 직접 스케치해보세요. 스케치가 끝나고 처리하다 버튼을 누르면 모델이 다운로드 되고 결과물이 출력됩니다. 랜덤 버튼을 눌러서 다른 생성 예시를 확인할 수도 있습니다.",
        "bookChapter": "텐서플로우, GAN, 실습, 그림",
        "bookPage": "149",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "スケッチを写真として",
            "description": "Pix2Pix GANモデルを利用してスケッチなどのソース画像を入力して他の形式の画像に変換するサービスです。",
            "howTo": "edges2cats、facadesなどの領域でソース画像の例と生成結果を確認できます。クリアボタンを押して既存のスケッチを消去して直接スケッチしてみてください。スケッチが終了して処理するボタンを押すとモデルがダウンロードされ、結果が出力ランダムボタンを押して他の作成例を確認することもできます。"
          },
          "en": {
            "title": "Sketch to Photo",
            "description": "This is a service that uses the Pix2Pix GAN model to receive input source images such as sketches and convert them into other types of images.",
            "howTo": "You can check source image examples and creation results in areas such as edges2cats, facades, etc. Click the erase button to erase the existing sketch and sketch it yourself. When the sketch is finished, click the process button to download the model and output the result. You can check other creation examples by clicking the random button."
          }
        }
      },
      {
        "name": "dash",
        "href": "/modules/dash/index.html",
        "title": "Dash 자율주행 자동차 시뮬레이터",
        "license": "MIT",
        "description": "WebGL과 Three.js로 구축된 자율주행 시뮬레이터입니다. 시뮬레이터는 정적 및 동적 장애물을 회피하고 목적지에 도달할 수 있도록 설계되었습니다.",
        "source": "https://github.com/mattbradley/dash",
        "howTo": "자동차는 WASD 키를 눌러 수동으로 조작할 수 있습니다. 자율주행 예제 시나리오를 보려면 오른쪽 아래 시나리오 로드를 누르고 예제 시나리오 탭을 눌러 8가지 중에 하나를 선택하세요. 시나리오 편집 버튼으로 새로운 시나리오를 만들 수도 있습니다.",
        "bookChapter": "시뮬레이터, 자율주행",
        "bookPage": "165",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "Dash 自律走行車シミュレータ",
            "description": "WebGLとThree.jsで構築された自律走行シミュレータです",
            "howTo": "自動車は WASD キーを押して手動で操作できます。 自律走行の例のシナリオを表示するには、右下のシナリオの読み込みをタップし、例のシナリオタブを押して 8 つのうちの 1 つを選択します。 シナリオ編集ボタンで新しいシナリオを作成することもできます。"
          },
          "en": {
            "title": "Dash self-driving car simulator",
            "description": "An autonomous driving simulator built with WebGL and Three.js. The simulator is designed to avoid static and dynamic obstacles and reach the destination.",
            "howTo": "The car can be operated manually by pressing the WASD keys. To view autonomous driving example scenarios, click Load Scenario at the bottom right and click the Example Scenarios tab to select one of eight scenarios. Use the Edit Scenario button to create a new scenario. You can make it too."
          }
        }
      },
      {
        "name": "streetscapeGl",
        "href": "/modules/streetscapeGl/index.html",
        "title": "streetscape.gl 자율주행 데이터수집 데모",
        "license": "MIT",
        "description": "KITTY와 NuScenes 데이터 세트를 streetscape.gl(자율주행 데이터를 시각화하기 위한 도구)을 이용해서 시각화한 자율주행 데모입니다.",
        "source": "https://github.com/prodramp/DeepWorks/tree/main/selfdrivingtech/streetscape.gl_demo",
        "howTo": "데모를 실행하고 화면 아래 상태 바에서 ▶버튼을 클릭하면 자동차가 움직입니다. 자동차가 움직이면 화면 왼쪽에 카메라 영상과 차량 정보가 표시되고, 화면 중앙에는 3차원 공간에서 움직이는 차량과 주변 사물들이 지도에 표시됩니다. 왼쪽 메뉴에서 모델과 사물의 보기(Streams) 여부를 변경할 수 있습니다.",
        "bookChapter": "시뮬레이터, 자율주행",
        "bookPage": "43, 160",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "streetscape.gl 自律走行データ収集デモ",
            "description": "KITTY と NuScenes データセットを streetscape.gl (自律走行データを視覚化するためのツール) を利用して視覚化した自律走行デモです。",
            "howTo": "デモを実行して画面下のステータスバーで▶ボタンをクリックすると車が動きます。車が動くと画面左側にカメラ映像と車両情報が表示され、画面中央には3次元空間で動く車両と周辺モノが地図上に表示されます。左側のメニューからモデルとモノのビュー（Streams）を変更できます。"
          },
          "en": {
            "title": "streetscape.gl autonomous driving data collection demo",
            "description": "This is an autonomous driving demo visualized using the KITTY and NuScenes datasets using streetscape.gl (a tool for visualizing autonomous driving data).",
            "howTo": "Run the demo and click the ▶ button in the status bar at the bottom of the screen to make the car move. When the car moves, camera images and vehicle information are displayed on the left side of the screen, and the moving vehicle and surroundings in three-dimensional space are displayed in the center of the screen. Objects will be displayed on the map. You can change whether models and objects are visible (Streams) in the left menu."
          }
        }
      },
      {
        "name": "selfParkingCarEvolution",
        "href": "/modules/selfParkingCarEvolution/index.html",
        "title": "자율 주차 차량의 진화",
        "license": "MIT",
        "description": "주차 학습 과정을 통해 유전 알고리즘의 작동 과정을 보여주는 앱입니다. 유전 알고리즘을 이용해서 자동차가 스스로 주차할 수 있도록 훈련됩니다.",
        "source": "https://github.com/trekhleb/self-parking-car-evolution",
        "howTo": "페이지를 열면 자동차가 스스로 주차하려는 모습을 볼 수 있습니다. 다른 차와 충돌하면 안되고 제한된 시간 내에 지정된 구역에 주차를 완료해야 합니다. 더 좋은 결과를 위해서 세대 크기나 그룹 크기 등의 설정 값을 변경할 수 있습니다. 수동 주차 탭에서는 WASD 키를 이용해 수동으로 주차해 볼 수도 있습니다.",
        "bookChapter": "학습, 자율주행",
        "bookPage": "",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "自律駐車車両の進化",
            "description": "駐車場学習過程を通じて遺伝アルゴリズムの動作過程を示すアプリです",
            "howTo": "ページを開くと、車が自分で駐車しようとしている様子を見ることができます。他の車と衝突しないで、限られた時間内に指定されたゾーンに駐車を完了する必要があります。値を変更できます。手動駐車タブでは、WASDキーを使用して手動で駐車することもできます。"
          },
          "en": {
            "title": "Evolution of autonomous parking vehicles",
            "description": "This app shows the operation of a genetic algorithm through a parking learning process. Using a genetic algorithm, a car is trained to park on its own.",
            "howTo": "When you open the page, you will see the car trying to park itself. It must not collide with other cars and must complete parking in the designated area within a limited time. For better results, set the household size, group size, etc. You can change the values. In the Manual Parking tab, you can also try parking manually using the WASD keys."
          }
        }
      },
      {
        "name": "fuzzy",
        "href": "https://apseren.itch.io/fuzzy",
        "title": "Fuzzy - 자율 주행의 윤리 문제",
        "license": "External Site",
        "description": "자율주행 중 발생할 수 있는 윤리적 문제 상황을 게임 형태로 보여주는 앱입니다. 정답이 있는 것은 아니고, 다른 사람의 선택도 확인할 수 있습니다.",
        "source": "https://apseren.itch.io/fuzzy",
        "howTo": "Run Game을 눌러 게임을 시작하세요. 19개의 상황 중 하나를 고를 수 있습니다. 각 상황에서 문제를 확인하고, 선택지들 중에서 나의 선택을 누르세요. 선택 이후 게임 속 자동차가 내 선택대로 움직이는 것을 볼 수 있습니다.",
        "bookChapter": "자율주행, 윤리",
        "bookPage": "174",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "Fuzzy - 自律走行の倫理問題",
            "description": "自律走行中に発生する可能性のある倫理的な問題の状況をゲーム形式で表示するアプリです。正解があるわけではなく、他の人の選択も確認できます。",
            "howTo": "Run Game を押してゲームを開始します。19 の状況のいずれかを選択できます。動いているのが見えます。"
          },
          "en": {
            "title": "Fuzzy - Ethical Issues in Autonomous Driving",
            "description": "This is an app that shows ethical issues that can arise during autonomous driving in the form of a game. There is no correct answer, and you can check other people's choices.",
            "howTo": "Click Run Game to start the game. You can choose one of 19 situations. Check the problem in each situation and press your choice among the options. After making your choice, the car in the game will change according to your choice. “You can see it moving."
          }
        }
      },
      {
        "name": "selfDrivingCarImageBrowser",
        "href": "https://cd-demo-self-driving.streamlit.app/",
        "title": "자율 주행 자동차 이미지 브라우저",
        "license": "Apache License 2.0",
        "description": "Udacity 자율주행차 데이터에 YOLO 카메라 객체 감지를 적용한 예입니다. 카메라 영상에서 여러 개체를 얼마나 잘 인식하는지 확인할 수 있습니다.",
        "source": "https://github.com/streamlit/demo-self-driving",
        "howTo": "화면 왼쪽 앱 모드 선택하기에서 앱 실행하기를 클릭하세요. 그러면 화면 오른쪽에 선택한 개체에 대해서 사람이 직접 보고 표시한 사진과, YOLO 모델이 표시한 사진이 나옵니다. 왼쪽의 프레임 영역에서 개체의 종류와 수, 프레임을 선택하면 다른 사진들의 결과를 확인할 수 있습니다.",
        "bookChapter": "자율주행",
        "bookPage": "162",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "自動運転車イメージブラウザ",
            "description": "Udacity 自律走行車データに YOLO カメラオブジェクト検出を適用した例です",
            "howTo": "画面左アプリモードを選択するには、アプリを実行する」をクリックします。画面右側に選択したオブジェクトについて人が直接見て表示した写真と、YOLOモデルが表示した写真が表示されます。オブジェクトの種類と数、フレームを選択すると、他の写真の結果を確認できます。"
          },
          "en": {
            "title": "Self-Driving Car Image Browser",
            "description": "This is an example of applying YOLO camera object detection to Udacity self-driving car data. You can see how well it recognizes multiple objects in camera images.",
            "howTo": "Click Run the app in the app mode selection on the left side of the screen. Then, a photo displayed by a person and a photo displayed by the YOLO model of the selected object will appear on the right side of the screen. In the frame area on the left, “You can select the type and number of objects and the frame to see the results in other photos."
          }
        }
      },
      {
        "name": "metaCar",
        "href": "/modules/metaCar/index.html",
        "title": "Meta Car 자율 주행 자동차 강화학습",
        "license": "None",
        "description": "여러 강화학습 알고리즘을 적용해서 자율주행 자동차를 훈련시켜볼 수 있습니다. 각각의 강화학습 과정과 그 결과를 확인 가능합니다.",
        "source": "https://github.com/thibo73800/metacar/tree/master",
        "howTo": "앱을 열면 ~ 액션이라는 이름이 붙은 총 4가지 예시가 있습니다. 예시 중 하나를 선택하세요. 예시에서는 Train을 눌러 직접 훈련시킬 수도 있고 Load trained agent를 눌러 훈련된 결과를 불러올 수도 있습니다. 이후 Play 버튼을 누르면 자동차가 훈련된 결과대로 움직입니다.",
        "bookChapter": "학습, 자율주행",
        "bookPage": "44, 168",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "Meta Car 自律走行車強化学習",
            "description": "複数の強化学習アルゴリズムを適用して自律走行車を訓練することができます。それぞれの強化学習過程とその結果を確認可能です。",
            "howTo": "アプリを開くと、〜アクションという名前の合計4つの例があります。例の1つを選択してください。その後、Playボタンを押すと、車が訓練された結果に移動します。"
          },
          "en": {
            "title": "Meta Car self-driving car reinforcement learning",
            "description": "You can train a self-driving car by applying various reinforcement learning algorithms. You can check each reinforcement learning process and its results.",
            "howTo": "When you open the app, there are a total of 4 examples named Actions. Select one of the examples. In the example, you can press Train to train it directly, or you can press Load trained agent to load the trained results. . Afterwards, when you press the Play button, the car moves according to the trained results."
          }
        }
      },
      {
        "name": "chatGpt",
        "href": "https://chat.openai.com",
        "title": "ChatGPT OpenAI 챗봇",
        "license": "External Site",
        "description": "ChatGPT는 OpenAI에서 개발한 인공지능 챗봇 서비스입니다. 많은 데이터로 학습한 GPT 모델을 이용했고, 사람과 유사하게 대화를 나눌 수 있습니다.",
        "source": "https://openai.com/blog/chatgpt",
        "howTo": "ChatGPT를 사용하려면 OpenAI 사이트에 가입해야 합니다. 가입 후 로그인하면 화면 아래 프롬프트 영역에 질문을 입력해보세요. 질문을 입력하면 ChatGPT가 어떤 주제의 대화이든 답변을 해줍니다. 새로운 주제로 대화를 시작하려면 왼쪽 위의 New Chat 버튼을 눌러 새로운 대화를 시작하세요.",
        "bookChapter": "생성형, 텍스트",
        "bookPage": "185",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "ChatGPT OpenAI チャットボット",
            "description": "ChatGPTはOpenAIによって開発された人工知能チャットボットサービスです。多くのデータで学習したGPTモデルを利用し、人と同様に会話を交わすことができます。",
            "howTo": "ChatGPTを使用するにはOpenAIサイトにサインアップする必要があります。サインアップ後にログインしたら、画面の下のプロンプト領域に質問を入力してください。開始するには、左上のNew Chatボタンを押して新しい会話を開始してください"
          },
          "en": {
            "title": "ChatGPT OpenAI Chatbot",
            "description": "ChatGPT is an artificial intelligence chatbot service developed by OpenAI. It uses a GPT model learned from a lot of data, and can have conversations similar to humans.",
            "howTo": "To use ChatGPT, you must sign up for the OpenAI site. After signing up and logging in, try entering a question in the prompt area at the bottom of the screen. When you enter a question, ChatGPT will answer any conversation on any topic. Start the conversation with a new topic. To get started, click the New Chat button in the top left to start a new conversation."
          }
        }
      },
      {
        "name": "dalle",
        "href": "https://openai.com/dall-e-2/",
        "title": "DALL·E 2 텍스트로 그림 생성",
        "license": "External Site",
        "description": "OpenAI가 개발한 이미지 생성형 AI 모델입니다. 많은 데이터로 학습했고, 텍스트 설명을 바탕으로 다양한 유형의 이미지를 생성할 수 있습니다.",
        "source": "https://openai.com/dall-e-2",
        "howTo": "DALL·E를 이용하려면 OpenAI 사이트에 가입해야 합니다. 그리고 credit이 충전 되어 있어야만 그림을 생성할 수 있습니다. 프롬프트 영역에 그림으로 표현하고 싶은 텍스트를 영어로 입력하세요. 이후 Generate 버튼을 누르면 credit이 소모되며 4개의 그림이 생성됩니다.",
        "bookChapter": "생성형, 그림",
        "bookPage": "",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "DALL・E 2 テキストで画像を生成する",
            "description": "OpenAIが開発した画像生成型AIモデルです。多くのデータで学習し、テキストの説明に基づいてさまざまな種類の画像を生成できます。",
            "howTo": "DALL・Eを利用するにはOpenAIサイトに参加しなければなりません。 そして、creditが充電されていなければ絵を生成できません。 プロンプト領域に絵で表現したいテキストを英語で入力してください。押すとクレジットが消費され、4つの画像が作成されます。"
          },
          "en": {
            "title": "DALL·E 2 Create pictures from text",
            "description": "This is an image generation AI model developed by OpenAI. It was trained with a lot of data and can generate various types of images based on text descriptions.",
            "howTo": "To use DALL·E, you must sign up for the OpenAI site. And you must have credit charged to create an image. Enter the text you want to express as an image in the prompt area in English. Then click the Generate button. When you press it, credit is consumed and 4 pictures are created."
          }
        }
      },
      {
        "name": "craiyon",
        "href": "https://www.craiyon.com",
        "title": "Craiyon 무료 이미지 생성",
        "license": "External Site",
        "description": "Craiyon은 무료 인공지능 이미지 생성 앱입니다. 이미지를 설명하는 키워드나 문구를 입력해서 이미지를 생성할 수 있습니다.",
        "source": "https://www.craiyon.com",
        "howTo": "광고가 많고 속도가 느릴 수 있지만, 로그인 없이 무료로 이미지를 생성할 수 있습니다. 영어로 이미지를 설명하는 키워드나 문구를 입력하고 Draw 버튼을 클릭하세요. 많이 알려져 있는 것을 구체적으로 묘사하면 원하는 이미지를 생성 할 수 있는 확률이 높아집니다.",
        "bookChapter": "생성형, 그림",
        "bookPage": "190",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "Craiyon無料画像を作成",
            "description": "Craiyonは無料の人工知能画像生成アプリです。画像を説明するキーワードやフレーズを入力して画像を生成できます。",
            "howTo": "広告が多く、速度が遅くなることがありますが、ログインせずに無料で画像を生成できます。英語で画像を説明するキーワードやフレーズを入力して Draw ボタンをクリックしてください。 よく知られていることを具体的に描写すると、希望の画像を生成する可能性が高くなります。"
          },
          "en": {
            "title": "Craiyon Free Image Creation",
            "description": "Craiyon is a free artificial intelligence image creation app. You can create images by entering keywords or phrases that describe the image.",
            "howTo": "It may have a lot of ads and be slow, but you can create images for free without logging in. Enter keywords or phrases that describe your image in English and click the Draw button. Be specific about what you're familiar with. This increases your chances of creating the image you want."
          }
        }
      },
      {
        "name": "bard",
        "href": "https://bard.google.com",
        "title": "Bard 구글 챗봇",
        "license": "External Site",
        "description": "구글과 딥마인드의 Gemini 프로를 기반으로 한 인공지능 챗봇 서비스입니다. 최신 정보도 제공하며, 한 질문에 3개의 답변을 출력해줍니다.",
        "source": "https://bard.google.com",
        "howTo": "Bard를 이용하려면 구글 로그인이 필요합니다. 로그인 후 프롬프트에 원하는 질문 을 입력하면 Bard가 답변해줍니다. 답변 위쪽의 다른 답안 보기를 클릭하면 해당 질문에 대한 총 3개의 답안을 함께 볼 수 있습니다. 프롬프트 왼쪽의 이미지 업로드 버튼으로 이미지를 업로드해 질문에 활용할 수 있습니다.",
        "bookChapter": "생성형, 텍스트",
        "bookPage": "188",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "Bard Google チャットボット",
            "description": "GoogleとディープマインドのGeminiプロをベースにした人工知能チャットボットサービスです。最新情報も提供し、1つの質問に3つの答えを出力します。",
            "howTo": "Bardを利用するにはGoogleログインが必要です。ログイン後にプロンプ​​トに希望の質問を入力するとBardが答えます。プロンプトの左側にある[画像のアップロード]ボタンを使用して画像をアップロードして質問に使用できます。"
          },
          "en": {
            "title": "Bard Google Chatbot",
            "description": "This is an artificial intelligence chatbot service based on Google and DeepMind's Gemini Pro. It also provides the latest information and prints three answers to one question.",
            "howTo": "To use Bard, you need to log in to Google. After logging in, enter the question you want in the prompt and Bard will answer it. If you click View other answers above the answer, you can view a total of three answers to that question. Yes. You can upload an image using the image upload button on the left of the prompt and use it to answer the question."
          }
        }
      },
      {
        "name": "newBing",
        "href": "https://www.microsoft.com/ko-kr/bing",
        "title": "빙 채팅 인공지능 검색 엔진",
        "license": "External Site",
        "description": "프로메테우스라는 GPT-4 기반의 검색 특화 모델을 탑재한 인공지능 검색 엔진입니다. 최신 정보와 정보의 출처를 함께 제공할 수 있습니다.",
        "source": "https://www.microsoft.com/ko-kr/bing",
        "howTo": "빙 채팅은 마이크로소프트 계정이 필요합니다. 그리고 Edge 브라우저에서 더 잘 작동합니다. 로그인 후 화면 하단의 입력창에 질문을 입력하면 질문과 관련된 답을 해줍니다. 답변의 길이가 다른 서비스에 비해 짧지만 하단에 출처 링크가 제공되어 보다 자세한 내용을 확인할 수 있습니다.",
        "bookChapter": "생성형, 텍스트",
        "bookPage": "186",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "ビングチャット人工知能検索エンジン",
            "description": "プロメテウスというGPT-4ベースの検索特化モデルを搭載した人工知能検索エンジンです。最新情報と情報のソースを一緒に提供できます。",
            "howTo": "Bing ChatはMicrosoftアカウントを必要とし、Edgeブラウザでうまく機能します。より短いですが、下部にソースリンクが提供され、より詳細な情報を確認できます。"
          },
          "en": {
            "title": "Bing Chat Artificial Intelligence Search Engine",
            "description": "It is an artificial intelligence search engine equipped with a GPT-4-based search specialized model called Prometheus. It can provide the latest information and sources of information.",
            "howTo": "Bing Chat requires a Microsoft account and works better in the Edge browser. After logging in, enter a question in the input box at the bottom of the screen and it will provide an answer related to the question. The length of the answer varies depending on the service. Although it is shorter, a source link is provided at the bottom so you can check out more details."
          }
        }
      },
      {
        "name": "clovaX",
        "href": "https://clova-x.naver.com",
        "title": "클로바 X 네이버 챗봇",
        "license": "External Site",
        "description": "네이버에서 개발한 한국어 언어모델 기반 인공지능 챗봇 서비스입니다. 플러그인 형태의 특화 서비스를 제공합니다.",
        "source": "https://clova-x.naver.com/welcome",
        "howTo": "클로바 X를 이용하려면 네이버 계정이 필요합니다. 네이버 로그인 후 하단의 입력창에 질문 내용을 입력하면 답변해줍니다. 문서 업로드 버튼으로 문서를 업로드해서 질문에 활용할 수 있고, 스킬 설정을 통해서 쇼핑이나 여행과 관련된 맞춤 답변을 받을 수 있습니다.",
        "bookChapter": "생성형, 텍스트",
        "bookPage": "189",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "クローバXネイバーチャットボット",
            "description": "ネイバーが開発した韓国語言語モデルベースの人工知能チャットボットサービスです。プラグイン型の特化サービスを提供します。",
            "howTo": "クローバXを利用するにはネイバーアカウントが必要です。ネイバーログイン後、下部の入力ウィンドウに質問内容を入力すると返信します。ドキュメントアップロードボタンでドキュメントをアップロードして質問に活用でき、スキル設定を通じてショッピングや旅行に関連したカスタム回答を受け取ることができます。"
          },
          "en": {
            "title": "Clova",
            "description": "This is an artificial intelligence chatbot service based on the Korean language model developed by Naver. It provides a specialized service in the form of a plug-in.",
            "howTo": "To use Clova You can receive personalized answers related to shopping or travel."
          }
        }
      },
      {
        "name": "bingImageCreator",
        "href": "https://www.bing.com/images/create",
        "title": "Bing Image Creator",
        "license": "External Site",
        "description": "DALL·E 3를 탑재한 이미지 생성 앱입니다. 사용자가 입력한 문장을 이미지로 변환할 수 있습니다.",
        "source": "https://www.bing.com/create",
        "howTo": "Edge 브라우저에서 마이크로소프트 계정으로 로그인해야 이용할 수 있습니다. 프롬프트는 한글로 입력해도 되지만, 영어로 입력하면 더욱 정확한 결과를 얻을 수 있습니다. 설명이 자세하고 세부 사항(예: 예술적 스타일)을 키워드 형태로 추가하면 원하는 이미지 생성 확률이 높아집니다.",
        "bookChapter": "생성형, 그림",
        "bookPage": "191",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "Bing Image Creator",
            "description": "DALL・E 3を搭載したイメージ生成アプリです。ユーザーが入力した文章をイメージに変換できます。",
            "howTo": "EdgeブラウザでMicrosoftアカウントでログインする必要があります。プロンプトはハングルで入力できますが、英語で入力するとより正確な結果が得られます。説明の詳細と詳細をキーワード形式で追加すると、必要な画像を生成する可能性が高くなります。"
          },
          "en": {
            "title": "Bing Image Creator",
            "description": "This is an image creation app powered by DALL·E 3. You can convert sentences entered by the user into images.",
            "howTo": "To use this, you must be logged in with a Microsoft account in the Edge browser. You can type the prompts in Korean, but you will get more accurate results if you type them in English. The instructions are detailed and detailed (e.g. artistic style) Adding in the form of keywords increases the probability of creating the desired image."
          }
        }
      },
      {
        "name": "wrtnai",
        "href": "https://wrtn.ai/",
        "title": "뤼튼 AI",
        "license": "External Site",
        "description": "다양한 언어 모델을 선택해서 활용할 수 있는 인공지능 기반의 콘텐츠 생성 플랫폼입니다. 채팅 뿐 아니라, 커스텀 툴과 챗봇 등의 기능이 있습니다.",
        "source": "https://wrtn.ai/",
        "howTo": "뤼튼을 이용하려면 이메일 또는 SNS 계정으로 회원 가입을 해야 합니다. 로그인 후 채팅 영역에서 GPT-4와 같은 모델을 선택하고 질문을 입력하면, 해당 모델을 이용해서 답변을 생성해줍니다. ~를 그려줘라고 질문하면 입력 문장을 참고해서 그림을 생성할 수도 있습니다.",
        "bookChapter": "생성형, 텍스트, 그림",
        "bookPage": "45, 180",
        "webcam": false,
        "lang": {
          "ja": {
            "title": "リュートン AI",
            "description": "さまざまな言語モデルを選択して活用できる人工知能ベースのコンテンツ生成プラットフォームです。チャットだけでなく、カスタムツールやチャットボットなどの機能があります。",
            "howTo": "リュートンを利用するには、EメールまたはSNSアカウントで会員登録する必要があります。を描いてくれと質問したら、入力文を参考にして絵を生成することもできます。"
          },
          "en": {
            "title": "Wtrn AI",
            "description": "It is an artificial intelligence-based content creation platform that allows you to select and use various language models. In addition to chat, it has features such as custom tools and chatbots.",
            "howTo": "To use Lutton, you must sign up with your email or SNS account. After logging in, select a model such as GPT-4 in the chat area and enter a question. An answer will be generated using that model. ~ If you ask Draw something, you can create a picture by referring to the input sentence."
          }
        }
      }
    ],
    sidebarCodeToName: {
      ko:{
        all: '', practice: '실습', learning: '학습', picture: '그림', music: '음악', recognition: '인식', tensorflow: '텐서플로우', dqn: 'DQN', cnn: 'CNN', rnn: 'RNN', gan: 'GAN', driving: '자율주행', generative: '생성형', noCamera: '웹캠 없음'
      },
      ja:{
        all: '', practice: '練習', learning: '学習', picture: '画像', music: '音楽', recognition: '認識', tensorflow: 'テンソルフロー', dqn: 'DQN', cnn: 'CNN', rnn: 'RNN', gan: 'GAN', driving: '自動運転', generative: '生成型', noCamera: 'カメラなし'
      },
      en:{
        all: '', practice: 'Practice', learning: 'Learning', picture: 'Image', music: 'Music', recognition: 'Recognition', tensorflow: 'TensorFlow', dqn: 'DQN', cnn: 'CNN', rnn: 'RNN', gan: 'GAN', driving: 'Autonomous', generative: 'Generative', noCamera: 'No Camera'
      }
    },
    sidebarNameToCode: {
      ko:{
        '': 'all', '실습': 'practice', '학습': 'learning', '그림': 'picture', '음악': 'music', '인식': 'recognition', '텐서플로우': 'tensorflow', 'DQN': 'dqn', 'CNN': 'cnn', 'RNN': 'rnn', 'GAN': 'gan', '자율주행': 'driving', '생성형': 'generative', '웹캠 없음': 'noCamera'
      },
      ja:{
        '': 'all', '練習': 'practice', '学習': 'learning', '画像': 'picture', '音楽': 'music', '認識': 'recognition', 'テンソルフロー': 'tensorflow', 'DQN': 'dqn', 'CNN': 'cnn', 'RNN': 'rnn', 'GAN': 'gan', '自動運転': 'driving', '生成型': 'generative', 'カメラなし': 'noCamera'
      },
      en:{
        '': 'all', 'Practice': 'practice', 'Learning': 'learning', 'Image': 'picture', 'Music': 'music', 'Recognition': 'recognition', 'TensorFlow': 'tensorflow', 'DQN': 'dqn', 'CNN': 'cnn', 'RNN': 'rnn', 'GAN': 'gan', 'Autonomous': 'driving', 'Generative': 'generative', 'No Camera': 'noCamera'
      }
    },
    bookChapterName: {
      rko: {"실습":"practice","DQN":"dqn","게임":"games","자율주행":"autonomous","학습":"learning","인식":"recognition","재미":"fun","물체":"object","손":"hand","얼굴":"face","자세":"pose","배경 분리":"backgroundIsolation","구분":"separation","표정":"facialExpression","영상":"image","그림":"picture","CNN":"cnn","RNN":"rnn","텐서플로우":"tensorFlow","음악":"music","GAN":"gan","시뮬레이터":"simulator","윤리":"ethics","생성형":"generative","텍스트":"text"},
      rja: {"実習":"practice","DQN":"dqn","ゲーム":"games","自動運転":"autonomous","学習":"learning","認識":"recognition","遊び":"fun","物体":"object","手":"hand","顔":"face","姿勢":"pose","背景の分離":"backgroundIsolation","区切り":"separation","表情":"facialExpression","映像":"image","画像":"picture","CNN":"cnn","RNN":"rnn","TF":"tensorFlow","音楽":"music","GAN":"gan","シミュレータ":"simulator","倫理":"ethics","生成型":"generative","テキスト":"text"},
      ren: {"Practice":"practice","DQN":"dqn","Games":"games","Autonomous":"autonomous","Learning":"learning","Recognition":"recognition","Fun":"fun","Object":"object","Hand":"hand","Face":"face","Pose":"pose","Isolation":"backgroundIsolation","Separation":"separation","Expression":"facialExpression","Image":"image","Picture":"picture","CNN":"cnn","RNN":"rnn","TensorFlow":"tensorFlow","Music":"music","GAN":"gan","Simulator":"simulator","Ethics":"ethics","Generative":"generative","Text":"text"},
      ko: {"practice":"실습","dqn":"DQN","games":"게임","autonomous":"자율주행","learning":"학습","recognition":"인식","fun":"재미","object":"물체","hand":"손","face":"얼굴","pose":"자세","backgroundIsolation":"배경 분리","separation":"구분","facialExpression":"표정","image":"영상","picture":"그림","cnn":"CNN","rnn":"RNN","tensorFlow":"텐서플로우","music":"음악","gan":"GAN","simulator":"시뮬레이터","ethics":"윤리","generative":"생성형","text":"텍스트"},
      ja: {"practice":"実習","dqn":"DQN","games":"ゲーム","autonomous":"自動運転","learning":"学習","recognition":"認識","fun":"遊び","object":"物体","hand":"手","face":"顔","pose":"姿勢","backgroundIsolation":"背景の分離","separation":"区切り","facialExpression":"表情","image":"映像","picture":"画像","cnn":"CNN","rnn":"RNN","tensorFlow":"TF","music":"音楽","gan":"GAN","simulator":"シミュレータ","ethics":"倫理","generative":"生成型","text":"テキスト"},
      en: {"practice":"Practice","dqn":"DQN","games":"Games","autonomous":"Autonomous","learning":"Learning","recognition":"Recognition","fun":"Fun","object":"Object","hand":"Hand","face":"Face","pose":"Pose","backgroundIsolation":"Isolation","separation":"Separation","facialExpression":"Expression","image":"Image","picture":"Picture","cnn":"CNN","rnn":"RNN","tensorFlow":"TensorFlow","music":"Music","gan":"GAN","simulator":"Simulator","ethics":"Ethics","generative":"Generative","text":"Text"}
    },
    lang: 'ko'
  },
  showLicenseToast(name, lang){
    try {
      if(sessionStorage.getItem('toast_' + name)){
        return;
      }

      const module = this.state.modules.find(x => x.name === name);
      /*if(module){
        sessionStorage.setItem('toast_' + name, 'true');
      }else{
        return;
      }*/

      let text = {license: '라이선스', source: '출처', introduction: '소개'};
      let title = module.title;
      let langHref = '';
      if(lang === 'ja'){
        text = {license: 'ライセンス', source: '出典', introduction: '紹介'};
        title = module.lang.ja.title;
        langHref = '/ja';
      }else  if(lang === 'en'){
        text = {license: 'License', source: 'Source', introduction: 'About'};
        title = module.lang.en.title;
        langHref = '/en';
      }

      iziToast.show({
        theme: 'dark',
        title: title,
        message: text.license + ': ' + module.license,
        position: 'topRight', // bottomRight, bottomLeft, topRight, topLeft, topCenter, bottomCenter
        progressBarColor: 'rgb(0, 255, 184)',
        buttons: [
          ['<button>' + text.source + '</button>', function (instance, toast) {
            window.open(module.source, '_blank');
          }, true],
          ['<button style="margin-left: 5px;">' + text.introduction + '</button>', function (instance, toast) {
            window.open(window.location.origin + langHref + '/article/' + module.name , '_blank');
          }, true]
        ]
      });
    } catch (e) {
      console.error(e);
    }
  }
}
