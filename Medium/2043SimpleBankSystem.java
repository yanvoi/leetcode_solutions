// practicing java again
class Bank {

    long[] balance;

    public Bank(long[] balance) {
        this.balance = balance;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if (!isAccountNumberValid(account1) || !isAccountNumberValid(account2)) return false;

        if (balance[account1 - 1] < money) return false;

        balance[account1 - 1] -= money;
        balance[account2 - 1] += money;
        return true;
    }
    
    public boolean deposit(int account, long money) {
        if (!isAccountNumberValid(account)) return false;

        balance[account - 1] += money;
        return true;
    }
    
    public boolean withdraw(int account, long money) {
        if (!isAccountNumberValid(account) || balance[account - 1] < money) return false;

        balance[account - 1] -= money;
        return true;
    }

    private boolean isAccountNumberValid(int account) {
        if (account > 0 && account <= balance.length) return true;
        return false;
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */
