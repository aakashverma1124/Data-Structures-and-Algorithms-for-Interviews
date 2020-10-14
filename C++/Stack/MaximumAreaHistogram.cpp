#include<bits/stdc++.h>
using namespace std;

int largest_area_histogram(int arr[],int n)
{
    int max_area = 0;
    int rb[n]; // nse on the right
    int lb[n]; // nse on the left
    stack<int> st;

    //for nser
    st.push(n - 1);
    rb[n - 1] = n;
    for (int i = n - 2; i >= 0; i--) {
      while (st.size() > 0 && arr[i] <= arr[st.top()]) st.pop();

      if (st.size() == 0) rb[i] = n;
      else rb[i] = st.top();
     
      st.push(i);
    }

    while(!st.empty()) st.pop(); //empty to reuse
    
    //for nsel
    st.push(0);
    lb[0] = -1;
    for (int i = 1; i < n; i++) {
      while (st.size() > 0 && arr[i] <= arr[st.top()]) st.pop();
      
      if (st.size() == 0) lb[i] = -1;
      else lb[i] = st.top();
     
      st.push(i);
    }

    //for max area
    for (int i = 0; i < n; i++) {
      int area = (rb[i] - lb[i] - 1) * arr[i];
      if (area > max_area) max_area = area;
    }

    return max_area;
    
}
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i = 0; i<n;i++)
        cin>>arr[i];
    
    int ans = largest_area_histogram(arr,n);
    cout<<ans;
}
