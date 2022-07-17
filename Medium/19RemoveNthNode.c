/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode *x = head;
    int i = 0;
    while(x != NULL)
    {
        i++;
        x = x->next;
    }
    {
        if(i == 0)
        {
            return NULL;
        }
        else if(i == 1 && n == 1)
        {
            head = NULL;
            return head;
        }
    }
    x = head;
    int how_much = i - n;
    if(how_much == 0)
    {
        head = x->next;
        return head;
    }
    else
    {
        for(int j = 0; j < how_much-1; j++)
        {
            x = x->next;
        }
        struct ListNode *y = x->next;
        x->next = y->next;
        return head;
    }
}
