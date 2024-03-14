using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BtnManager : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void OnClickCnt()
    {
        Debug.Log("카운트 증가");
    }

    public void OnClickQuit()
    {
        Application.Quit();
    }
}
