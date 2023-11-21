using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class poseDetecting : MonoBehaviour
{
    // Start is called before the first frame update
    public UDPReceive udpReceive;
    public GameObject[] humanPoints;


    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        // 데이터 받아오기
        string data = udpReceive.data;
        // 문자열 data 괄호제거
        data = RemoveBrackets(data);
        // ','를 기준으로 나눈다.
        string[] points = data.Split(',');

        for (int i = 0; i < 33; i++)
        {
            float x = float.Parse(points[i * 3 + 2]) * 10 * -1;
            float y = float.Parse(points[i * 3 + 1]) * 10 * -1;
            float z = float.Parse(points[i * 3]) * 10;
            

            humanPoints[i].transform.localPosition = new Vector3(x, y, z);
        }

    }

    string RemoveBrackets(string input)
    {
        // 대괄호와 소괄호 제거
        input = input.Replace("[", "").Replace("]", "").Replace("(", "").Replace(")", "");
        return input;
    }
}
