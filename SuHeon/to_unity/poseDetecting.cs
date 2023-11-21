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
        // ������ �޾ƿ���
        string data = udpReceive.data;
        // ���ڿ� data ��ȣ����
        data = RemoveBrackets(data);
        // ','�� �������� ������.
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
        // ���ȣ�� �Ұ�ȣ ����
        input = input.Replace("[", "").Replace("]", "").Replace("(", "").Replace(")", "");
        return input;
    }
}
