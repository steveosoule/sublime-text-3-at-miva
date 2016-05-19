Emporium Plus TOOLKIT v5 `Sublime Text 2` `Snippets`
=====================

A [Sublime Text 2](http://sublimetext.com/2) snippet library for the popular [Miva Merchant](http://mivamerchant.com) module by [Emporium Plus](http://emporiumplus.com).  

Installation
------------

* Download the Snippets via ZIP, SSH, or `git clone`
* Copy all snippets into your

		* `~/Library/Application\ Support/Sublime\ Text 2/Packages/<bundle_subdir>` ( OS X )
		* `<user>\AppData\Roaming\Sublie Text 2\Packages\User\<bundle_subdir>` ( WIN )

Usage
-----
These stippets are not bound to a specific filetype.  To avoid conflicts with other snippet libraries, the 'tk-' leader is prepended to all snippet names.

`tk-functionname`

For example, typing:

	tk-attr + TAB

expands:

	<mvt:item name="toolkit" param="attr|acount|l.all_settings:product:id" />

Hitting `TAB` or `SHIF + TAB` will toggle through the function parameters.  In this case, starting with `account` and concluding on `l.all_settings:product:id`

__NOTE__ The leader is `tk-` because dash preserves ST2 auto-complete and suggestions.  , / . : all break this

Contribution
------------

If you find a bug please open an issue or email —  [&#109;&#099;&#104;&#097;&#110;&#064;&#109;&#105;&#118;&#097;&#109;&#101;&#114;&#099;&#104;&#097;&#110;&#116;&#046;&#099;&#111;&#109;](&#109;&#099;&#104;&#097;&#110;&#064;&#109;&#105;&#118;&#097;&#109;&#101;&#114;&#099;&#104;&#097;&#110;&#116;&#046;&#099;&#111;&#109;)


###—chan