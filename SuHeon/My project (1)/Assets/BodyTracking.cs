using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HandTracking : MonoBehaviour
{
    // Start is called before the first frame update
    public UDPReceive udpReceive;
    public GameObject[] bodyPoints;
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        string data = udpReceive.data;

        data = data.Remove(0, 1);
        data = data.Remove(data.Length-1, 1);
        print(data);
        string[] points = data.Split(',');
        print(points[0]);

        for ( int i = 0; i<bodyPoints.Length; i++)
        {

            float x = float.Parse(points[i * 3])*10;
            float y = float.Parse(points[i * 3 + 1])*10*-1;
            float z = 100;

            bodyPoints[i].transform.localPosition = new Vector3(x, y, z);

        }


    }
}