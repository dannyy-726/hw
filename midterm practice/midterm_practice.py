{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "bf477029",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mKeyboardInterrupt\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[4]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;66;03m#write a function that takes a list of integers and returns a new list contain only the even numbers\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m nums = \u001b[38;5;28;43minput\u001b[39;49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mprovide a list of numbers\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[32m      3\u001b[39m num_lst = []\n\u001b[32m      5\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mevens\u001b[39m(nums):\n",
      "\u001b[36mFile \u001b[39m\u001b[32m/opt/anaconda3/envs/dsci510/lib/python3.12/site-packages/ipykernel/kernelbase.py:1275\u001b[39m, in \u001b[36mKernel.raw_input\u001b[39m\u001b[34m(self, prompt)\u001b[39m\n\u001b[32m   1273\u001b[39m     msg = \u001b[33m\"\u001b[39m\u001b[33mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m   1274\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(msg)\n\u001b[32m-> \u001b[39m\u001b[32m1275\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_input_request\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m   1276\u001b[39m \u001b[43m    \u001b[49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mprompt\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1277\u001b[39m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43m_parent_ident\u001b[49m\u001b[43m[\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mshell\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1278\u001b[39m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mget_parent\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mshell\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   1279\u001b[39m \u001b[43m    \u001b[49m\u001b[43mpassword\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m,\u001b[49m\n\u001b[32m   1280\u001b[39m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m/opt/anaconda3/envs/dsci510/lib/python3.12/site-packages/ipykernel/kernelbase.py:1320\u001b[39m, in \u001b[36mKernel._input_request\u001b[39m\u001b[34m(self, prompt, ident, parent, password)\u001b[39m\n\u001b[32m   1317\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[32m   1318\u001b[39m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[32m   1319\u001b[39m     msg = \u001b[33m\"\u001b[39m\u001b[33mInterrupted by user\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m-> \u001b[39m\u001b[32m1320\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(msg) \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[32m   1321\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[32m   1322\u001b[39m     \u001b[38;5;28mself\u001b[39m.log.warning(\u001b[33m\"\u001b[39m\u001b[33mInvalid Message:\u001b[39m\u001b[33m\"\u001b[39m, exc_info=\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[31mKeyboardInterrupt\u001b[39m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "#write a function that takes a list of integers and returns a new list contain only the even numbers\n",
    "nums = input(\"provide a list of numbers\")\n",
    "num_lst = []\n",
    "\n",
    "def evens(nums):\n",
    "\n",
    "    for num in nums:\n",
    "        if num % 2 == 0:\n",
    "            num_lst.append(num)\n",
    "        return num_lst\n",
    "    print(num_lst)\n",
    "evens()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "105a72d4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "dsci510",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
