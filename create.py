import os
import argparse

# Configuration
LOCAL_REPO_PATH = "/home/kishore/kishore/Atcoder"  # Replace with your local Atcoder repo path
CP_TEMPLATE = """
#include <bits/stdc++.h>
using namespace std;

/* clang-format off */

/* TYPES  */
#define ll long long
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vi vector<int>
#define vll vector<long long>
#define mii map<int, int>
#define si set<int>
#define sc set<char>

/* FUNCTIONS */
#define f(i,s,e) for(long long int i=s;i<e;i++)
#define cf(i,s,e) for(long long int i=s;i<=e;i++)
#define rf(i,e,s) for(long long int i=e-1;i>=s;i--)
#define pb push_back
#define eb emplace_back

/* PRINTS */
template <class T>
void print_v(vector<T> &v) { cout << "{"; for (auto x : v) cout << x << ","; cout << "\\b}"; }

/* UTILS */
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795
#define read(type) readInt<type>()
ll min(ll a,int b) { if (a<b) return a; return b; }
ll min(int a,ll b) { if (a<b) return a; return b; }
ll max(ll a,int b) { if (a>b) return a; return b; }
ll max(int a,ll b) { if (a>b) return a; return b; }
ll gcd(ll a,ll b) { if (b==0) return a; return gcd(b, a%b); }
ll lcm(ll a,ll b) { return a/gcd(a,b)*b; }
string to_upper(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='a' && a[i]<='z') a[i]-='a'-'A'; return a; }
string to_lower(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='A' && a[i]<='Z') a[i]+='a'-'A'; return a; }
bool prime(ll a) { if (a==1) return 0; for (int i=2;i<=round(sqrt(a));++i) if (a%i==0) return 0; return 1; }
void yes() { cout<<"YES\\n"; }
void no() { cout<<"NO\\n"; }

/*  All Required define Pre-Processors and typedef Constants */
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int  uint64;

/* clang-format on */

/* Main()  function */
int main()
{

\t#ifndef ONLINE_JUDGE
\tfreopen("inputf.in","r",stdin);
\t//freopen("outputf.in","w",stdout);
\t#endif

\tint tc;
\ttc = read(int);

\twhile(tc--){
\t\twrite(tc);
\t}
\treturn 0;
}
/* Main() Ends Here */
"""

def create_and_setup_contest(contest_name, problems):
    # Navigate to the local repo
    os.chdir(LOCAL_REPO_PATH)

    # Create a new folder for the contest if it doesn't exist
    contest_folder = os.path.join(LOCAL_REPO_PATH, contest_name)
    if not os.path.exists(contest_folder):
        os.makedirs(contest_folder)
        print(f"Folder '{contest_name}' created.")
    else:
        print(f"Folder '{contest_name}' already exists.")

    # Create problem files with CP template
    for problem in problems:
        problem_file = os.path.join(contest_folder, f"{problem}.cpp")
        if not os.path.exists(problem_file):
            with open(problem_file, "w") as f:
                f.write(CP_TEMPLATE)
            print(f"Created file: {problem_file}")
        else:
            print(f"File {problem_file} already exists.")

    # Create inputf.in and outputf.in files
    input_file = os.path.join(contest_folder, "inputf.in")
    output_file = os.path.join(contest_folder, "outputf.in")
    
    if not os.path.exists(input_file):
        open(input_file, "w").close()
        print(f"Created file: {input_file}")
    else:
        print(f"File {input_file} already exists.")

    if not os.path.exists(output_file):
        open(output_file, "w").close()
        print(f"Created file: {output_file}")
    else:
        print(f"File {output_file} already exists.")

def main():
    # Argument parser for the contest name and problem identifiers
    parser = argparse.ArgumentParser(description="Automate setting up Atcoder solutions.")
    parser.add_argument("contest_name", type=str, help="Name of the contest (e.g., abc190).")
    parser.add_argument(
        "-p", "--problems", nargs="+", default=["A", "B", "C", "D", "E", "F"],
        help="List of problem identifiers to create files for (default: A, B, C, D, E, F)."
    )
    args = parser.parse_args()

    # Call the function to set up the contest
    create_and_setup_contest(args.contest_name, args.problems)

if __name__ == "__main__":
    main()

