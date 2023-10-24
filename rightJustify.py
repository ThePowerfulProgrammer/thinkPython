#Write a function named right_justify that takes a string named s as a parameter and 
#prints the string with enough leading spaces so that the last letter of the string is in 
#column 70 of the display.
#>>> right_justify('allen')
# allen

def right_justify(s,justifyLength):
    length = len(s);
    totalSpace = justifyLength-length;
    print(" "*totalSpace+s);
    return "";
    
    
int removeDuplicatesTest2(vector<int> nums)
{
    int firstUnique = nums.front();
    int secondUnique = firstUnique;
    int position = 0;
    int index = 1;

    while (position + index < nums.size() && secondUnique != nums.back())
        {
            while (nums[position + index] == firstUnique)
                {
                    index +=1;
                }
            secondUnique = nums[position+index];
            cout << "First: " << firstUnique << " ---- " << position << "-" << index << " ----- " << " Second: " << secondUnique << endl;

            if (index > 2) {
                cout << "Length pre erasure: " << nums.size() << endl;
                nums.erase(nums.begin() + position + 2, nums.begin() + position + index);
                cout << "Length post erasure: " << nums.size() << endl;

                // Update variables for the next iteration based on the updated vector
                index = 1;
                secondUnique = nums[position + index];
            }
            else {
                // Update variables for the next iteration
                firstUnique = secondUnique;
                position += index;
                index = 1;
            }
        }

    for (int &num: nums)
        {
            cout << num << " " ;
        }
    cout << endl;
    return 0;
}

print(right_justify("Ashish",70));