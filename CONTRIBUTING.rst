How to contribute
=================

How to setup commit hook
------------------------

.. code-block:: console

   $ mkdir -p .git/hooks/
   $ ln -s `pwd`/hooks/pre-commit .git/hooks/


How to download dependencies
----------------------------

.. code-block:: console

   $ pip install -e .


The Perils of Rebasing
----------------------

Do not rebase commits that you have pushed to a public repository.

Refer http://git-scm.com/book/en/Git-Branching-Rebasing#The-Perils-of-Rebasing

Use

.. code-block:: console

   $ git pull --rebase


How to deal with 'No Newline at End of File'
------------

According to POSIX, You should add the **line terminator**, EOL(end of line, `\n`), at the end of file.

I referenced [this blog](http://robots.thoughtbot.com/no-newline-at-end-of-file) to follow this rule.

* For Vim users, you’re all set out of the box! Just don’t change your `eol` setting.
* For Emacs users, add `(setq require-final-newline t)` to your `.emacs` or `.emacs.d/init.el` file.
* For TextMate users, you can install the [Avian Missing Bundle](https://github.com/elia/avian-missing.tmbundle#strip-trailing-whitespace-on-save) and add `TM_STRIP_WHITESPACE_ON_SAVE = true` to your `.tm_properties` file.
* For Sublime users, `set the ensure_newline_at_eof_on_save` option to `true`.
* For RubyMine, set “Ensure line feed at file end on Save” under “Editor.”


