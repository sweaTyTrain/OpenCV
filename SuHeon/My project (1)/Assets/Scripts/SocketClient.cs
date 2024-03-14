using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Android;
using System;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading;

public class SorketClient : MonoBehaviour
{
    WebCamTexture camTexture;
    public RawImage cameraViewImage;


    public string host = "118.37.219.113";
    public int port = 5053;

    private Socket clientSocket;
    private Thread clientThread;
    private bool alive = true;

    public string data;

    void Start()
    {
        clientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
        clientSocket.Connect(host, port);

        CameraOn();
    }

    void Update()
    {
        SendVideoFrame();
    }

    void SendVideoFrame()
    {
        if (camTexture != null && camTexture.isPlaying)
        {
            // 비디오 프레임을 텍스처로 변환
            Texture2D tex = new Texture2D(camTexture.width, camTexture.height, TextureFormat.RGB24, false);
            tex.SetPixels(camTexture.GetPixels());
            tex.Apply();

            int width = tex.width;
            int height = tex.height;

            Debug.Log(height);
            Debug.Log(width);

            // 이미지의 픽셀을 순회하며 RGB 값을 추출하여 배열에 저장
            Color[] pixels = tex.GetPixels();
            Debug.Log(pixels.Length);
            byte[] imageData = new byte[pixels.Length * 3];
            int index = 0;
            foreach (Color pixel in pixels)
            {
                imageData[index++] = (byte)(pixel.r * 255);
                imageData[index++] = (byte)(pixel.g * 255);
                imageData[index++] = (byte)(pixel.b * 255);
            }

            // 서버로 RGB 값을 전송
            clientSocket.Send(imageData);
        }
    }

    private void ClientRun()
    {
        // Loop to send data
        while (alive)
        {
            // You can add your own data processing logic here.
            // For simplicity, I'm omitting the data processing part.
            // You may implement your data processing logic here.

            // For example, sending dummy data to the server
            string data = "Dummy data from Unity";
            byte[] bytes = System.Text.Encoding.UTF8.GetBytes(data);
            clientSocket.Send(bytes);

            Thread.Sleep(1000); // Adjust the interval as needed
        }
    }

    public void CameraOn()
    {   
        if (!Permission.HasUserAuthorizedPermission(Permission.Camera))
        {
            Permission.RequestUserPermissions(new string[] { Permission.Camera });
        }

        if (WebCamTexture.devices.Length == 0)
        {
            return;
        }
        
        WebCamDevice[] devices = WebCamTexture.devices;
        int selectedCameraIndex = -1;
        for (int i = 0; i < devices.Length; i++)
        {
            if (!devices[i].isFrontFacing)
            {
                selectedCameraIndex = i;
                break;
            }
        }
        if (selectedCameraIndex >= 0)
        {
            camTexture = new WebCamTexture(devices[selectedCameraIndex].name);
            camTexture.requestedFPS = 60;
            cameraViewImage.texture = camTexture;
            camTexture.Play();
        }
    }

    public void CameraOff()
    {
        if (camTexture != null)
        {
            camTexture.Stop();
            WebCamTexture.Destroy(camTexture);
            camTexture = null;
        }
    }

    

    void OnApplicationQuit()
    {
        // Close the socket connection when the application quits
        alive = false;
        clientThread.Join();
        clientSocket.Close();
        Debug.Log("Socket connection closed");
    }
}
