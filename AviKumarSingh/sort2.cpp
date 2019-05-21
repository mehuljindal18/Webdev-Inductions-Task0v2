#include <bits/stdc++.h>

using namespace std;

int main()
{
    int a[100],n,i,j,temp,min,minind;
    cout<<"Enter the number of elements : ";
    cin>>n;
    cout<<"\nEnter elements of the array : \n";
    for(i=0;i<n;i++)
    cin>>a[i];

    for(i=0;i<(n-1);i++)
    {
        minind=i;
        for(j=i+1;j<n;j++)
        {
            if(a[j]<a[minind])
            minind=j;
        }
        
            temp=a[i];
            a[i]=min;
            min=temp;
        
    }

	for(i=0;i<n;i++)
	{
		cout<<a[i]<<" ";
	}
    return 0;
}
